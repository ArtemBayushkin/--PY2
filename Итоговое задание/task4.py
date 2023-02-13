class Entity:
    """Base class for all entities"""

    def __init__(self, name: str):
        """
        :param name: entity name
        """
        """Constructor for Entity class"""
        self.name = name

    def __str__(self) -> str:
        """String representation of Entity class"""
        return f"Entity {self.name}"

    def __repr__(self) -> str:
        """Representation of Entity class"""
        return f"Entity({self.name})"


class Vehicle(Entity):
    """A vehicle entity"""

    def __init__(self, name: str, wheels: int):
        """
        :param name: entity name
        :param wheels: number of wheel
        Constructor for Vehicle class"""
        super().__init__(name)
        if not isinstance(wheels, int):
            raise ValueError("Number of wheels must be an integer")
        if wheels < 0:
            raise ValueError("Number of wheels cannot be less than 0")
        else:
            self.wheels = wheels

    def __str__(self) -> str:
        """String representation of Vehicle class"""
        return f"Vehicle {self.name} with {self.wheels} wheels"

    def __repr__(self) -> str:
        """Representation of Vehicle class"""
        return f"Vehicle({self.name}, {self.wheels})"

    def get_wheels(self) -> int:
        """Returns the number of wheels of the vehicle
        Overloads the __str__ method of the base class to return the number of wheels of the vehicle.
        """
        return self.wheels

print(Vehicle("BMX", 2))
