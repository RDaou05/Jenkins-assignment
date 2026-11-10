"""Simple calculator functions exercised by the CI pipeline."""


def add_numbers(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract_numbers(a, b):
    """Return a minus b."""
    return a - b


def multiply_numbers(a, b):
    """Return the product of a and b."""
    return a * b


def divide_numbers(a, b):
    """Return a divided by b. Raises ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power_numbers(a, b):
    """Return a raised to the power b."""
    return a ** b


def main():
    print("Application started")
    print("2 + 3 =", add_numbers(2, 3))
    print("7 - 4 =", subtract_numbers(7, 4))
    print("6 * 5 =", multiply_numbers(6, 5))
    print("8 / 2 =", divide_numbers(8, 2))
    print("2 ^ 10 =", power_numbers(2, 10))


if __name__ == "__main__":
    main()
