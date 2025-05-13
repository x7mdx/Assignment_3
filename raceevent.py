class RaceEvent:
        """ Class Represent A RaceEvent"""

    def __init__(self, event_id, location, date, capacity):
        """ Constructor for PurchaseOrder class """
        self.event_id = event_id
        self.location = location
        self.date = date  
        self.capacity = capacity
        self.tickets_sold = 0

    def is_available(self):
        """ check if any ticket available for this event or not. """
        return self.tickets_sold < self.capacity

    def sell_ticket(self, quantity=1):
        """ Method to Sell a ticket """
        if self.tickets_sold + quantity <= self.capacity:
            self.tickets_sold += quantity
            return True
        else:
            print("Not enough tickets available.")
            return False
