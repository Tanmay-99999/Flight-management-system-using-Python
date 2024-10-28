class Passenger:
    def __init__(self, passenger_id, name, passport_number):
        self.passenger_id = passenger_id
        self.name = name
        self.passport_number = passport_number
class Node:
    def __init__(self, passenger=None):
        self.passenger = passenger
        self.next = None
class PassengerManagement:
    def __init__(self):
        self.head = None
    def add_passenger(self, passenger):
        new_node = Node(passenger)
        new_node.next = self.head
        self.head = new_node
    def remove_passenger(self, passenger_id):
        current = self.head
        prev = None
        while current:
            if current.passenger.passenger_id == passenger_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    def get_passenger(self, passenger_id):
        current = self.head
        while current:
            if current.passenger.passenger_id == passenger_id:
                return current.passenger
            current = current.next
        return None
    def list_passengers(self):
        passengers = []
        current = self.head
        while current:
            passengers.append(current.passenger)
            current = current.next
        return passengers
    
    def get_passenger(self, passenger_id):
        for passenger in self.passengers:
            if passenger.passenger_id == passenger_id:
                return passenger
        return None