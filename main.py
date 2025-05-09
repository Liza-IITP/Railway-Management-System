from manager import RailwaySystem
from data import load_data

if __name__ == "__main__":
    print("Hey , Liza this side from Railway Booking System, how can I help you?")
    system = RailwaySystem()
    load_data(system)
    system.go()
    print("Thank you for using the Railway Booking System!")