#This is my 3rd project
# Simple Calculator (+, -, *, /).

a= eval(input("Enter a : "))
b= eval(input("Enter b : "))
operation = input("Enter Operation (+,-,*,/) : ")

if operation == "+" :
    result = a + b
elif operation == "-" :
    result = a - b
elif operation == "*" :
    result = a * b 
elif operation == "/" :
    if b == 0 :
        result = "Error : Division by Zero !"
    else :
        result = a / b

else :
    result = "Invalid Operation "
print("Answer Is : ",result)