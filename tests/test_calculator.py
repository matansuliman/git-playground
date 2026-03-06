from app.calculator import add, divide, multiply, power, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 2) == 3


def test_divide():
    assert divide(10, 2) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_power():
    assert power(2, 3) == 8
