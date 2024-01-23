#!/usr/bin/python3

def raise_exception():
    try:
        # Attempt to perform an operation that raises a type exception
        result = "string" + 42  # This will raise a TypeError
    except TypeError as e:
        print(f"Exception raised: {e}")

# Example usage:
raise_exception()

