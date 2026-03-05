from app.calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 2) == 3


def test_divide():
    assert divide(10, 2) == 5