import tkinter as tk
from gui import FlightBookingGUI
def main():
    root = tk.Tk()
    app = FlightBookingGUI(root)

    root.mainloop()
if __name__ == "__main__":
    main()