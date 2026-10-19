# This is 10th Project.
# Login EnterFace project

correct_username = "anup"
correct_password = "2007"

attempts = 0
max_attempts = 3

while attempts < max_attempts :
    username = input("Enter Username : ")
    password = input("Enter Password : ")

    if username == correct_username and password == correct_password :
        print("Login Successful ! Welcome. ")
        break

    else :
        attempts += 1
        reamining = max_attempts - attempts
        if reamining > 0 :
            print(f" Wrong Credentials. {reamining} attempts left. ")

        else :
            print("Account locked. Too Many failed attempts. ")