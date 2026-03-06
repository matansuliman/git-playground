from app.trigonometry_functions import cos, sin, tan


def test_sin():
    assert sin(0) == 0

def test_cos():
    assert cos(0) == 1

def test_tan():
    assert tan(0) == 0
