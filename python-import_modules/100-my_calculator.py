#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Dictionary mapping operators to functions
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Check if operator is valid
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform calculation
    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
