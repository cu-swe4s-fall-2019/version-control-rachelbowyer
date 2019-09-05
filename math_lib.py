import sys


def div(a, b):
    if b == 0:
        print("Error, divide by zero encountered")
        sys.exit(1)
        return None
    else:
        return a/b

def add(a, b):
    return a+b
