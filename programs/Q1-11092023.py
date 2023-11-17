class Vehicle:
    def __init__(self, name, mileage, total_seats):
        '''
        Set seat numbers to the all the vehicles.
        '''
        self.name = name
        self.mileage = mileage
        self.seats = total_seats

    def totalFare(self):
        '''
        Find total fare of vehicle based on total number of seats
        '''
        self.fare = self.seats * 100

class Bus(Vehicle):
    def totalFare(self):
        '''
        Find fare of bus: 10% more of basic fare
        '''
        super().totalFare()
        self.fare += self.fare / 10
        return self.fare

b = Bus('volvo', 20, 50)
print("Total bus fare is:", b.totalFare())












