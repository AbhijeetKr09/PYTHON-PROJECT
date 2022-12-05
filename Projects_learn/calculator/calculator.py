from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    n1 = float(input("Enter first number: "))
    for operators in operations:
        print(operators)
    start_with_first = True
    while start_with_first:
        operations_symbol = input("Pick an operation from above: ")
        n2 = float(input("Enter second number: "))

        calculation = operations[operations_symbol]
        answer = calculation(n1, n2)
        print(f"{n1} {operations_symbol} {n2} = {round(answer, 2)}")
        start = input(
            f"Want to continue with the number {round(answer, 2)}. y for yes and n to start a new calculation. ").lower()
        if start == "y":
            n1 = answer
        else:
            start_with_first = False
            calculator()


calculator()
