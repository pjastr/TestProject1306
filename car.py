class Car:
    """Klasa opisująca samochody."""

    def __init__(self, serial, capacity):
        self.serial = serial
        self.capacity = capacity

    def load(self, good :int) ->None:
        """Metoda ładująca."""
        pass

    def __str__(self):
        return f"Car: {self.serial},{self.capacity}"

