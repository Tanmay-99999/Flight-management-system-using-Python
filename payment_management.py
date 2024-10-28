class Payment:
    def __init__(self, payment_id, booking_id, amount):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
class PaymentManagement:
    def __init__(self):
        self.payments = []
    def add_payment(self, payment):
        self.payments.append(payment)
    def remove_payment(self, payment_id):
        self.payments = [payment for payment in self.payments if
payment.payment_id != payment_id]
    def get_payment(self, payment_id):
        for payment in self.payments:
            if payment.payment_id == payment_id:
                return payment
            return None
    def list_payments(self):
        return self.payments
    def get_payment_by_booking_id(self, booking_id):
        for payment in self.payments:
            if payment.booking_id == booking_id:
                return payment
        return None