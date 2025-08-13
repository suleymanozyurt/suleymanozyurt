"""Simple calculator module."""

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run basic arithmetic operations.")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("operator", choices=["+", "-", "*", "/"], help="Arithmetic operator")
    parser.add_argument("b", type=float, help="Second operand")
    args = parser.parse_args()

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    result = operations[args.operator](args.a, args.b)
    print(result)
