class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, capacity):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.full_tank = self.capacity

    def drive(self, distance):
        fuel_needed = (10 / 100) * distance 
        if fuel_needed > self.capacity:
            return f'Not enough fuel to drive {distance} km. Please refuel.'
        
        self.capacity -= fuel_needed
        return f'Drove {distance} km. Remaining fuel: {self.capacity} liters.'

    def refuel(self, liters):
        empty_space = self.full_tank-self.capacity
        if liters > empty_space:
            self.capacity = self.full_tank
            return f'Full tank'
        if liters < empty_space:
            self.capacity +=liters

        return f'The current amount of fuel is {self.capacity}'


car1 = Car('BMW', 'm30', 1990, 'benzin', 50)
print(car1.drive(50))
print(car1.drive(50))

print(car1.refuel(2))