from enum import Enum

class OrderStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

class PurchaseOrder:
    def __init__(self, order_id, customer, tickets, total_amount, status, order_date):
        self.order_id = order_id
        self.customer = customer  
        self.tickets = tickets  
        self.total_amount = total_amount
        self.status = status  
        self.order_date = order_date

    def update_status(self, new_status):
        self.status = new_status

    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        self.total_amount += ticket.calculate_price()

    def remove_ticket(self, ticket_id):
        for t in self.tickets:
            if t.ticket_id == ticket_id:
                self.total_amount -= t.calculate_price()
                self.tickets.remove(t)
                break
