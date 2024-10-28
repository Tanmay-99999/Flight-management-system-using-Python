class Flight:
    def __init__(self, flight_id, destination, departure_time, capacity):
        self.flight_id = flight_id
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.passengers = []
class FlightManagement:
    def __init__(self):
        self.flights = []
    def add_flight(self, flight):
        self.flights.append(flight)
    def remove_flight(self, flight_id):
        self.flights = [flight for flight in self.flights if flight.flight_id
!= flight_id]
    def get_flight(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
            return None
    def list_flights(self):
        return self.flights
    def get_flight(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None