from enum import Enum

class TicketType(Enum):
    SINGLE_RACE = "Single Race"
    WEEKEND_PACKAGE = "Weekend Package"
    SEASON_MEMBERSHIP = "Season Membership"
    GROUP_DISCOUNT = "Group Discount"


class Ticket:
    def __init__(self, ticket_id, ticket_type, price, features, validity, event):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type 
        self.price = price
        self.features = features  
        self.validity = validity
        self.event = event 

    def calculate_price(self):
        return self.price
