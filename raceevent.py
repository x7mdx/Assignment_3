class RaceEvent:
    def __init__(self, event_id, location, date, capacity):
        self.event_id = event_id
        self.location = location
        self.date = date  
        self.capacity = capacity
        self.tickets_sold = 0

    def is_available(self):
        return self.tickets_sold < self.capacity

    def sell_ticket(self, quantity=1):
        if self.tickets_sold + quantity <= self.capacity:
            self.tickets_sold += quantity
            return True
        else:
            print("Not enough tickets available.")
            return False
