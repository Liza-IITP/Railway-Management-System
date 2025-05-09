from trains import Train
from route import Route
from schedule import Schedule

def load_data(system):
    route1 = Route(["Chennai","Mumbai","Delhi", "Kanpur", "Varanasi"])
    schedule1 = Schedule(["Monday", "Friday"], "08:00", "18:00")
    train1 = Train("101", "Chennai Express", route1, schedule1, 100)

    route2 = Route(["Mumbai", "Surat", "Ahmedabad"])
    schedule2 = Schedule(["Tuesday", "Saturday"], "09:00", "17:00")
    train2 = Train("202", "Deccan Express", route2, schedule2, 80)

    system.add_train(train1)
    system.add_train(train2)