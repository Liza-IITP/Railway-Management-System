from ticket import Ticket
from person import Person


class User(Person):
    def __init__(self, name, age, gender, user_id):
        super().__init__(name, age, gender,user_id)
        self.bookings = []

    def book_ticket(self, train, date):
        if train.book_seat():
            ticket = Ticket(self.user_id, train, date)
            self.bookings.append(ticket)
            print("Ticket booked !")
            ticket.display_ticket()
        else:
            print(" No seats available!")

    def cancel_ticket(self, ticket_id):
        for ticket in self.bookings:
            if ticket.ticket_id == ticket_id:
                self.bookings.remove(ticket)
                print("Ticket Cancelled!")
                return
        print(" Ticket ID not found.")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings yet.")
        for ticket in self.bookings:
            ticket.display_ticket()
