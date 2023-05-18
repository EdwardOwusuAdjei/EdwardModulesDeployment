from moduleB.main import multiply

def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(-2, 2) == -4
    assert multiply(0, 2) == 0
