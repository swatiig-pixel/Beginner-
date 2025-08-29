def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


operation_dictionary = {
    "+" : add ,
    "-" : subtract ,
    "*" : multiply ,
    "/" : divide
}

num1 = float(input("What is the first number? :"))
for symbol in operation_dictionary:
    print(symbol)
operation = input("Pick an operation : ")
num2 = float(input("What is the next number?: "))
answer = operation_dictionary[operation](num1,num2)

print(f"{num1} {operation} {num2} = {answer}")