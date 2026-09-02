#This is 4rt Project.
# ATM Withdrawal Simulator

balance = 10000
correct_pin = "2007"

pin = input("Enter your 4-digit PIN : ")

if pin == correct_pin :
    while True :
        print("\n 1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choise = input("Choose an option : ")

        if choise == "1" :
            print(f"Your balance is ₹{balance}")

        elif choise == "2" :
            amount = float(input("Enter amount to Withdraw : "))
            if amount > balance :
                print("Insufficient funds!")
            elif amount % 100 != 0:
                print("Please enter amount in multiples of 100")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully. New balance : ₹{balance}")

        elif choise == "3" :
            amount = float(input("Enter amount to deposite : "))
            balance+=amount
            print(f"₹{amount} deposite successfully. New balance : ₹{balance}")

        elif choise == "4" :
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

else :
    print("Incorrect PIN. Access denied.") 