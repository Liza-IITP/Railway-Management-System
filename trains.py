class Train:
    def __init__(self, train_id, name, route, schedule, total_seats):
        self.train_id = train_id
        self.name = name
        self.route = route           
        self.schedule = schedule     
        self.total_seats = total_seats
        self.seats_available = total_seats

    def display_details(self):
        print(f"\n Train: {self.name} | ID: {self.train_id}")
        print(f"Seats Available: {self.seats_available}/{self.total_seats}")
        self.route.display_route()
        self.schedule.display_schedule()

    def check_availability(self):
        return self.seats_available > 0

    def book_seat(self):
        if self.seats_available > 0:
            self.seats_available -= 1
            return True
        return False

    def cancel_seat(self):
        if self.seats_available < self.total_seats:
            self.seats_available += 1
