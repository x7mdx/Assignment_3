import pickle


def load_users():
    try:
        with open("users.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return {}
    
print("\n\n=====Users Binary File data======")

print(load_users())

ORDER_DATA_FILE = "orders.pkl"

def load_orders():
    try:
        with open(ORDER_DATA_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return []
    
print("\n\n=====Orders Binary File data======")   
print(load_orders())

def load_discounts():
    try:
        with open("discounts.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return []

print("=====Discounts Binary File data======")
for d in load_discounts():
    print(d.__dict__)



