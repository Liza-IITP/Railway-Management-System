class Route:
    def __init__(self, stations):
        self.stations = stations  # List 

    def get_full_route(self):
        return " → ".join(self.stations)

    def display_route(self):
        print("Route:")
        for i, station in enumerate(self.stations, 1):
            print(f"{i}. {station}")
