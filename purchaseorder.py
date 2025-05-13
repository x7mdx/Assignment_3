from enum import Enum

class OrderStatus(Enum):
    """ Types of Order Status """
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

class PurchaseOrder:
    """ Class Represent an Order Purchase"""
    def __init__(self, order_id, customer, tickets, total_amount, status, order_date):
        """ Constructor for PurchaseOrder class """
        self.order_id = order_id
        self.customer = customer  
        self.tickets = tickets  
        self.total_amount = total_amount
        self.status = status  
        self.order_date = order_date

    def update_status(self, new_status):
        """
        setter for status attribute.
        """
        self.status = new_status

    def add_ticket(self, ticket):
        """
        Method to add ticket in an Order Purchase
        """
        self.tickets.append(ticket)
        self.total_amount += ticket.calculate_price()

    
    def remove_ticket(self, ticket_id):
        """
        Method to remove ticket in an Order Purchase
        """
        for t in self.tickets:
            if t.ticket_id == ticket_id:
                self.total_amount -= t.calculate_price()
                self.tickets.remove(t)
                break
