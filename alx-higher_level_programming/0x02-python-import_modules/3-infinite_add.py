#!/usr/bin/python3
import sys


def add_arguments(arguments):
    return sum(int(arg) for arg in arguments)

if __name__ == "__main__":
    
    result = add_arguments(sys.argv[1:])

    
    print(result)

