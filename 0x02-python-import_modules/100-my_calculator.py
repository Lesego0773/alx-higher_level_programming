#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def calculate_result(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return sub(a, b)
    elif operator == "*":
        return mul(a, b)
    elif operator == "/":
        return div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Calculate result and print
    result = calculate_result(a, operator, b)
    print("{} {} {} = {}".format(a, operator, b, result))

