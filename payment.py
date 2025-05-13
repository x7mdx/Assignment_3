from enum import Enum
from purchaseorder import OrderStatus

class PaymentMethod(Enum):
    """ Different Types of Payment Method """
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    DIGITAL_WALLET = "Digital Wallet"


class Payment:
    """Class Represent a Payment"""

    """
    A Constructor for Payment class
    """
    def __init__(self, payment_id, order, amount, payment_method, payment_date):
        self.payment_id = payment_id
        self.order = order  
        self.amount = amount
        self.payment_method = payment_method  
        self.payment_date = payment_date  


    """
    method to process the payment.
    """
    def process_payment(self):
        print(f"Processing payment of {self.amount} for Order ID: {self.order.order_id}")
        self.order.update_status(OrderStatus.CONFIRMED)
        print("Payment successful. Order confirmed.")
