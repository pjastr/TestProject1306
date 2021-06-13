import car

p1 = car.Car("Ac", 23)
p1.serial = "abc"
p1.load(2)
print(len(p1.serial))
car.Car.load(p1, 12)
print(p1)
