from moduleC.main import subtract

def test_subtract():
    assert subtract(2, 2) == 0
    assert subtract(-2, 2) == -4
    assert subtract(0, 2) == -2