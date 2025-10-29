# Integrate JSON based logger with an XML based system

# Existing class (incompatible interface)
class XMLLogger:
    def log_xml(self, xml_data):
        print(f"Logging data in XML format: {xml_data}")

# Target interface expected by our application
class JSONLoggerInterface:
    def log(self, data):
        pass

# Adapter to convert JSON data to XML format
class JSONtoXMLAdapter(JSONLoggerInterface):
    def __init__(self, xml_logger):
        self.xml_logger = xml_logger

    def log(self, data):
        # Convert JSON (dict) to a simple XML string for demo
        xml_data = "<log>" + "".join([f"<{k}>{v}</{k}>" for k, v in data.items()]) + "</log>"
        self.xml_logger.log_xml(xml_data)

# Client code
if __name__ == "__main__":
    xml_logger = XMLLogger()
    adapter = JSONtoXMLAdapter(xml_logger)

    log_data = {"event": "login", "user": "admin"} # JSON log data
    adapter.log(log_data)
