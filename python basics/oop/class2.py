class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passengers(self, name):
        if not self.capacity:
            return False
        self.passengers.append(name)
        self.capacity -= 1
        return True
    def rem_seat(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(5)
person = ['Sayeed', 'akash', 'rudro', 'morsalin','sazzad', 'abdulliah']
for p in person:
    success = flight.add_passengers(p)
    if success:
        print(f'seat booked for {p}')
    else:
        print(f'the capacity is exceed so seat cant be booked for {p}')

    
        