from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


# Concrete Class 1
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to Credit Card.")

# Concrete Class 2
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")

    def refund(self, amount):
        print(f"Refunded ₹{amount} via PayPal.")

# Concrete Class 3
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to UPI account.")


# --- Usage ---
def process_payment(payment_method: Payment, amount: float):
    payment_method.pay(amount)
    payment_method.refund(amount)

# Test
cc = CreditCardPayment()
process_payment(cc, 500)

paypal = PayPalPayment()
process_payment(paypal, 1000)

upi = UPIPayment()
process_payment(upi, 250)
