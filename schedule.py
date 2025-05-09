class Schedule:
    def __init__(self, days_available, departure_time, arrival_time):
        self.days_available = days_available  
        self.departure_time = departure_time 
        self.arrival_time = arrival_time    

    def display_schedule(self):
        print(f"Days Available : {', '.join(self.days_available)}")
        print(f"Departure Time : {self.departure_time}")
        print(f"Arrival Time   : {self.arrival_time}")
