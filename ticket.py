import uuid
from datetime import datetime

class Ticket:
    def __init__(self, user_id, train, travel_date):
        self.ticket_id = str(uuid.uuid4())[:8]
        self.user_id = user_id
        self.train_id = train.train_id
        self.train_name = train.name
        self.travel_date = travel_date
        self.booking_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_ticket(self):
        print(f"\n Ticket ID: {self.ticket_id}")
        print(f"User ID     : {self.user_id}")
        print(f"Train       : {self.train_name} ({self.train_id})")
        print(f"Travel Date : {self.travel_date}")
        print(f"Booked At   : {self.booking_time}")
