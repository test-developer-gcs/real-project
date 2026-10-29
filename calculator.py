
def add(a, b):
    return a - b  # Bug: should be addition


def subtract(a, b):
    return a + b  # Bug: should be subtraction


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))


if __name__ == "__main__":
    main()
