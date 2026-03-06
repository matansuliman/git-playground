from .trigonometry_functions import sin, cos, tan


def add(a, b):
    return a + b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def multiply(a, b):
    return a * b


def power(a, b):
    return a ** b