'''
Smart City Monitoring System

🎯 Objective

We're designing a Smart City Monitoring System that:

    Tracks various city devices (streetlights, cameras, air sensors, etc.)
    Collects their status efficiently
    Shows them in a hierarchical zone view
    Handles external data format incompatibility
    Uses caching to avoid slow API calls

This realistic problem lets us demonstrate multiple structural patterns working together.

'''

# Shared device configurations
# Flyweight pattern - Each sensor (light, camera, etc.) has shared properties like model, firmware, and manufacturer.


class DeviceType:
    def __init__(self, device_type, model, manufacturer):
        self.device_type = device_type
        self.model = model
        self.manufacturer = manufacturer

class DeviceTypeFactory:
    _types = {}

    @staticmethod
    def get_device_type(device_type, model, manufacturer):
        key = (device_type, model, manufacturer)
        if key not in DeviceTypeFactory._types:
            DeviceTypeFactory._types[key] = DeviceType(device_type, model, manufacturer)
        return DeviceTypeFactory._types[key]

# -------------------------------------------------------------------------------------------------------------
# Integrate third party sensors
# A third-party company provides air-quality sensors with a different interface.

# Third-party sensor (incompatible format)
class ThirdPartyAirSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def external_status(self):
        return {"sensor": self.sensor_id, "pm2.5": 42, "status": "OK"}

# Our common Device interface
class Device:
    def get_status(self):
        pass

# Adapter to unify third-party API
class AirSensorAdapter(Device):
    def __init__(self, third_party_sensor, device_type):
        self.sensor = third_party_sensor
        self.device_type = device_type

    def get_status(self):
        data = self.sensor.external_status()
        return f"AirSensor[{data['sensor']}] Status: {data['status']}, PM2.5: {data['pm2.5']}"

# -------------------------------------------------------------------------------------------------------------

# Some devices (like streetlights) fetch data from a slow cloud API.
# We’ll use a Proxy to cache recent results.

import time

class StreetLight(Device):
    def __init__(self, light_id, device_type):
        self.light_id = light_id
        self.device_type = device_type

    def get_status(self):
        time.sleep(1)  # Simulate slow API
        return f"StreetLight[{self.light_id}] is ON"

# Proxy adds caching
class StreetLightProxy(Device):
    def __init__(self, real_light):
        self.real_light = real_light
        self._cached_status = None
        self._last_updated = 0

    def get_status(self):
        if time.time() - self._last_updated > 5:  # refresh every 5 sec
            print("Fetching new status from API...")
            self._cached_status = self.real_light.get_status()
            self._last_updated = time.time()
        else:
            print("Returning cached status...")
        return self._cached_status

# -------------------------------------------------------------------------------------------------------------

'''

We’ll represent our smart city as a hierarchy:

    City (root)
        Zone 1 (branch)
            Devices (leaves)

Composite allows uniform operations across all levels.

'''

class CityComponent:
    def show_status(self):
        pass

class Zone(CityComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show_status(self):
        print(f"\n📍 Zone: {self.name}")
        for child in self.children:
            child.show_status()

class CityDevice(CityComponent):
    def __init__(self, device):
        self.device = device

    def show_status(self):
        print(f" - {self.device.get_status()}")


# -------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Shared device types (Flyweight)
    air_type = DeviceTypeFactory.get_device_type("AirSensor", "AQ-100", "EnviroTech")
    light_type = DeviceTypeFactory.get_device_type("StreetLight", "LUX-300", "Philips")

    # Create devices
    sensor1 = AirSensorAdapter(ThirdPartyAirSensor("AS-01"), air_type)
    light1 = StreetLightProxy(StreetLight("ST-01", light_type))
    light2 = StreetLightProxy(StreetLight("ST-02", light_type))

    # Create zones (Composite)
    zone1 = Zone("Downtown")
    zone1.add(CityDevice(sensor1))
    zone1.add(CityDevice(light1))

    zone2 = Zone("Uptown")
    zone2.add(CityDevice(light2))

    # Root City Composite
    city = Zone("SmartCity")
    city.add(zone1)
    city.add(zone2)

    # Show status
    city.show_status()
    city.show_status()
