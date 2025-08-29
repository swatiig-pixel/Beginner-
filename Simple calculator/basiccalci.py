print("Hey welcome \n Here you can do basic calculations \n Type exit to stop the calculation")

while True:
    num1 = input("\n\nEnter the first number or type exit to stop :")
    if num1 == "exit":
        print("Thank you! \n See you again")
        break

    num1= float(num1)
    operator = input("Enter the operator:")
    if operator not in ["+","-","*","/"]:
        print("You gave a invalid operator. Try again")
        continue

    num2 = float(input("Enter the second number:"))


    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1/num2
        if num2 == 0:
            print("Division by zero is not allowed")
            continue

    print(f"The rusult is {result}")        
        