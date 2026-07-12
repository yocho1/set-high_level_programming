#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    num_args = len(argv) - 1  # Exclude script name

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
