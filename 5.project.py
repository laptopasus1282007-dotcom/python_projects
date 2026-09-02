movies = {
    "1": {"name" : "Toxic", "price" : 200},
    "2": {"name" : "Spiderman", "price" : 250},
    "3": {"name": "Intersteller", "price": 220}

}
print("🎬 Available Movies:")
for key, value in movies.items():
    print(f"{key}. {value['name']} - ₹{value['price']} per ticket")

choice = input("ENter movie number to book : ")

if choice in movies :
    movies = movies[choice]
    tickets = int(input(f"How many tickets for {movies ['name']}? "))

    total = movies['price'] * tickets

    print(f"\nBooking Summary : ")
    print(f"Movie : {movies['name']}")
    print(f"Tickets : {tickets}")
    print(f"Total Price : ₹{total}")

    confirm = input("COnfirm booking? (yes/no) : ")
    if confirm.lower() == "yes":
        print("✅ Booking confirmed! Enjoy your movie🍿")
    else:
        print("❌ Booking Cancelled.")

else :
    print("Invalid Movie selction. ")
