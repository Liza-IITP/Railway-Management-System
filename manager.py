from user import User
from trains import Train
from route import Route
from schedule import Schedule

class RailwaySystem:
    def __init__(self):
        self.users = {}
        self.trains = {}

    def go(self):
        while True:
            print("\n===== Railway Booking System =====")
            print("1. Register User")
            print("2. Login User")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.login_user()
            elif choice == "3":
                break
            else:
                print(" Invalid choice.")

    def register_user(self):
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        user_id = input("Choose a User ID: ")

        if user_id in self.users:
            print(" User ID already exists!")
            return

        user = User(name, age, gender, user_id)
        self.users[user_id] = user
        print(" Registered successfully!")

    def login_user(self):
        user_id = input("Enter User ID: ")
        if user_id not in self.users:
            print(" User not found.")
            return

        user = self.users[user_id]
        while True:
            print(f"\n--- Welcome {user.name} ---")
            print("1. Book Ticket")
            print("2. Cancel Ticket")
            print("3. View Bookings")
            print("4. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.book_ticket(user)
            elif choice == "2":
                ticket_id = input("Enter Ticket ID: ")
                user.cancel_ticket(ticket_id)
            elif choice == "3":
                user.view_bookings()
            elif choice == "4":
                break
            else:
                print(" Invalid choice.")

    def book_ticket(self, user):
        if not self.trains:
            print(" No trains available.")
            return

        print("\nAvailable Trains:")
        for train in self.trains.values():
            train.display_details()

        train_id = input("Enter Train ID to book: ")
        if train_id not in self.trains:
            print(" Invalid Train ID")
            return

        travel_date = input("Enter Travel Date (YYYY-MM-DD): ")
        user.book_ticket(self.trains[train_id], travel_date)

    def add_train(self, train):
        self.trains[train.train_id] = train
