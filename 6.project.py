#This is 6th project.
#Food ordeer system.

menu = {
    "1": {"name": "Burger", "price": 120},
    "2": {"name": "Pizza", "price": 250},
    "3": {"name": "Pasta", "price": 180},
    "4": {"name": "Cold Drink", "price": 60},
    "5": {"name": "Momos", "price": 90},
    "6": {"name": "Maggie", "price": 50},
    "7": {"name": "Fride Rice", "price": 60},
    "8": {"name": "paneer roll", "price": 120}
    
    
    
}

cart=[]
total=0

print("Welcome to Food Order system")
print("Menu : ")
for key, value in menu.items():
    print(f"{key}. {value['name']} - {value['price']}")


while True:
    choice = input("\nEnter item number to add  (or 'done' to finish): ")
    if choice.lower() == "done":
        break

    if choice in menu :
        item =menu[choice]
        cart.append(item['name'])
        total += item['price']
        print(f"{item['name']} added to cart ! ")

    else:
        print("Invalid choice,try again.")

if cart :
    print("\n Order Summary : ")
    for item in cart : 
        print(f"- {item}")

    gst = total * 0.05
    final_total = total + gst 

    print(f"\nSubtotal : {total}")
    print(f"GST (5%) : {gst:.2f}")
    print(f"Total Amount : {final_total:.2f}")

else:
    print("No items ordered.")
