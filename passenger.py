from car import Car


class PassengerCar(Car):

    def load(self, passengers):
        self.capacity += passengers

    def __str__(self):
        return f"PassengerCar: {self.serial},{self.capacity}"