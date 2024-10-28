from collections import deque
class Booking:
    def __init__(self, booking_id, passenger_id, flight_id):
        self.booking_id = booking_id
        self.passenger_id = passenger_id
        self.flight_id = flight_id
class BookingManagement:
    def __init__(self):
        self.bookings = deque()
    def add_booking(self, booking):
        self.bookings.append(booking)
    def cancel_booking(self, booking_id):
        self.bookings = deque([booking for booking in self.bookings if
booking.booking_id != booking_id])
    def get_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None
    def list_bookings(self):
        return list(self.bookings)