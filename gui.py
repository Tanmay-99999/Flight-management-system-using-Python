# gui.py
import tkinter as tk
from tkinter import messagebox, ttk
from flight_management import Flight, FlightManagement
from booking_management import Booking, BookingManagement
from passenger_management import Passenger, PassengerManagement
from payment_management import Payment, PaymentManagement

class FlightBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking Management")
        
        self.flight_management = FlightManagement()
        self.booking_management = BookingManagement()
        self.passenger_management = PassengerManagement()
        self.payment_management = PaymentManagement()

        self.create_widgets()

    def create_widgets(self):
       
        self.tab_control = ttk.Notebook(self.root)
        
       
        self.flight_tab = ttk.Frame(self.tab_control)
        self.booking_tab = ttk.Frame(self.tab_control)
        self.passenger_tab = ttk.Frame(self.tab_control)
        self.payment_tab = ttk.Frame(self.tab_control)
        
        
        self.tab_control.add(self.flight_tab, text='Flights')
        self.tab_control.add(self.booking_tab, text='Bookings')
        self.tab_control.add(self.passenger_tab, text='Passengers')
        self.tab_control.add(self.payment_tab, text='Payments')
        
        self.tab_control.pack(expand=1, fill="both")

        self.create_flight_widgets()
        self.create_booking_widgets()
        self.create_passenger_widgets()
        self.create_payment_widgets()

    def create_flight_widgets(self):
        tk.Label(self.flight_tab, text="Flight Management").grid(row=0, column=0, columnspan=2)

        tk.Label(self.flight_tab, text="Flight ID").grid(row=1, column=0)
        self.flight_id_entry = tk.Entry(self.flight_tab)
        self.flight_id_entry.grid(row=1, column=1)

        tk.Label(self.flight_tab, text="Destination").grid(row=2, column=0)
        self.destination_entry = tk.Entry(self.flight_tab)
        self.destination_entry.grid(row=2, column=1)

        tk.Label(self.flight_tab, text="Departure Time").grid(row=3, column=0)
        self.departure_time_entry = tk.Entry(self.flight_tab)
        self.departure_time_entry.grid(row=3, column=1)

        tk.Label(self.flight_tab, text="Capacity").grid(row=4, column=0)
        self.capacity_entry = tk.Entry(self.flight_tab)
        self.capacity_entry.grid(row=4, column=1)

        tk.Button(self.flight_tab, text="Add Flight", command=self.add_flight).grid(row=5, column=0)
        tk.Button(self.flight_tab, text="List Flights", command=self.list_flights).grid(row=5, column=1)

    def create_booking_widgets(self):
        tk.Label(self.booking_tab, text="Booking Management").grid(row=0, column=0, columnspan=2)

        tk.Label(self.booking_tab, text="Booking ID").grid(row=1, column=0)
        self.booking_id_entry = tk.Entry(self.booking_tab)
        self.booking_id_entry.grid(row=1, column=1)

        tk.Label(self.booking_tab, text="Passenger ID").grid(row=2, column=0)
        self.booking_passenger_id_entry = tk.Entry(self.booking_tab)
        self.booking_passenger_id_entry.grid(row=2, column=1)

        tk.Label(self.booking_tab, text="Flight ID").grid(row=3, column=0)
        self.booking_flight_id_entry = tk.Entry(self.booking_tab)
        self.booking_flight_id_entry.grid(row=3, column=1)

        tk.Button(self.booking_tab, text="Add Booking", command=self.add_booking).grid(row=4, column=0)
        tk.Button(self.booking_tab, text="List Bookings", command=self.list_bookings).grid(row=4, column=1)

    def create_passenger_widgets(self):
        tk.Label(self.passenger_tab, text="Passenger Management").grid(row=0, column=0, columnspan=2)

        tk.Label(self.passenger_tab, text="Passenger ID").grid(row=1, column=0)
        self.passenger_id_entry = tk.Entry(self.passenger_tab)
        self.passenger_id_entry.grid(row=1, column=1)

        tk.Label(self.passenger_tab, text="Name").grid(row=2, column=0)
        self.passenger_name_entry = tk.Entry(self.passenger_tab)
        self.passenger_name_entry.grid(row=2, column=1)

        tk.Label(self.passenger_tab, text="Passport Number").grid(row=3, column=0)
        self.passport_number_entry = tk.Entry(self.passenger_tab)
        self.passport_number_entry.grid(row=3, column=1)

        tk.Button(self.passenger_tab, text="Add Passenger", command=self.add_passenger).grid(row=4, column=0)
        tk.Button(self.passenger_tab, text="List Passengers", command=self.list_passengers).grid(row=4, column=1)

    def create_payment_widgets(self):
        tk.Label(self.payment_tab, text="Payment Management").grid(row=0, column=0, columnspan=2)

        tk.Label(self.payment_tab, text="Payment ID").grid(row=1, column=0)
        self.payment_id_entry = tk.Entry(self.payment_tab)
        self.payment_id_entry.grid(row=1, column=1)

        tk.Label(self.payment_tab, text="Booking ID").grid(row=2, column=0)
        self.payment_booking_id_entry = tk.Entry(self.payment_tab)
        self.payment_booking_id_entry.grid(row=2, column=1)

        tk.Label(self.payment_tab, text="Amount").grid(row=3, column=0)
        self.amount_entry = tk.Entry(self.payment_tab)
        self.amount_entry.grid(row=3, column=1)

        tk.Button(self.payment_tab, text="Add Payment", command=self.add_payment).grid(row=4, column=0)
        tk.Button(self.payment_tab, text="List Payments", command=self.list_payments).grid(row=4, column=1)

    def add_flight(self):
        flight_id = self.flight_id_entry.get()
        destination = self.destination_entry.get()
        departure_time = self.departure_time_entry.get()
        capacity = int(self.capacity_entry.get())

        flight = Flight(flight_id, destination, departure_time, capacity)
        self.flight_management.add_flight(flight)

        messagebox.showinfo("Success", "Flight added successfully!")

    def list_flights(self):
        flights = self.flight_management.list_flights()
        flight_info = "\n".join([f"{flight.flight_id}: {flight.destination} at {flight.departure_time}" for flight in flights])
        messagebox.showinfo("Flights", flight_info)

    def add_booking(self):
        booking_id = self.booking_id_entry.get()
        passenger_id = self.booking_passenger_id_entry.get()
        flight_id = self.booking_flight_id_entry.get()

        booking = Booking(booking_id, passenger_id, flight_id)
        self.booking_management.add_booking(booking)

        messagebox.showinfo("Success", "Booking added successfully!")

    def list_bookings(self):
        bookings = self.booking_management.list_bookings()
        booking_info = "\n".join([f"Booking ID: {booking.booking_id}, Passenger ID: {booking.passenger_id}, Flight ID: {booking.flight_id}" for booking in bookings])
        messagebox.showinfo("Bookings", booking_info)

    def add_passenger(self):
        passenger_id = self.passenger_id_entry.get()
        name = self.passenger_name_entry.get()
        passport_number = self.passport_number_entry.get()

        passenger = Passenger(passenger_id, name, passport_number)
        self.passenger_management.add_passenger(passenger)

        messagebox.showinfo("Success", "Passenger added successfully!")

    def list_passengers(self):
        passengers = self.passenger_management.list_passengers()
        passenger_info = "\n".join([f"Passenger ID: {passenger.passenger_id}, Name: {passenger.name}, Passport Number: {passenger.passport_number}" for passenger in passengers])
        messagebox.showinfo("Passengers", passenger_info)

    def add_payment(self):
        payment_id = self.payment_id_entry.get()
        booking_id = self.payment_booking_id_entry.get()
        amount = float(self.amount_entry.get())

        payment = Payment(payment_id, booking_id, amount)
        self.payment_management.add_payment(payment)

        messagebox.showinfo("Success", "Payment added successfully!")

    def list_payments(self):
        payments = self.payment_management.list_payments()
        payment_info = "\n".join([f"Payment ID: {payment.payment_id}, Booking ID: {payment.booking_id}, Amount: {payment.amount}" for payment in payments])
        messagebox.showinfo("Payments", payment_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightBookingGUI(root)
    root.mainloop()
