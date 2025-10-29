
'''
In a 2D video game, thousands of enemies (like soldiers) appear on the screen.
Each soldier has:
    The same sprite (image), weapon type, and animation (intrinsic data)
    But different positions, health, and direction (extrinsic data)
    Without the Flyweight pattern, each soldier would have its own copy of the sprite and animation data, wasting memory.

Use the Flyweight Pattern to share common data (sprite, animation, weapon) 
between multiple soldiers while maintaining unique state (position, health).

'''



# Flyweight: shared intrinsic state
class SoldierType:
    def __init__(self, name, weapon, sprite):
        self.name = name
        self.weapon = weapon
        self.sprite = sprite  # large image data

    def render(self, x, y):
        print(f"Rendering {self.name} with {self.weapon} at ({x},{y})")


# Flyweight Factory
class SoldierFactory:
    _soldier_types = {}

    @staticmethod
    def get_soldier_type(name, weapon, sprite):
        key = (name, weapon, sprite)
        if key not in SoldierFactory._soldier_types:
            print(f"Creating new SoldierType: {name}, {weapon}")
            SoldierFactory._soldier_types[key] = SoldierType(name, weapon, sprite)
        return SoldierFactory._soldier_types[key]


# Context: contains extrinsic data
class Soldier:
    def __init__(self, x, y, health, soldier_type: SoldierType):
        self.x = x
        self.y = y
        self.health = health
        self.soldier_type = soldier_type

    def draw(self):
        print(f"Soldier at ({self.x},{self.y}) with health {self.health}")
        self.soldier_type.render(self.x, self.y)


# Client code
if __name__ == "__main__":
    # Create thousands of soldiers efficiently
    soldiers = []

    infantry_type = SoldierFactory.get_soldier_type("Infantry", "Rifle", "infantry_sprite.png")
    sniper_type = SoldierFactory.get_soldier_type("Sniper", "Sniper Rifle", "sniper_sprite.png")

    # Create 5 soldiers of each type
    for i in range(5):
        soldiers.append(Soldier(i * 10, i * 5, 100, infantry_type))
        soldiers.append(Soldier(i * 15, i * 7, 80, sniper_type))

    # Draw them all
    for s in soldiers:
        s.draw()
