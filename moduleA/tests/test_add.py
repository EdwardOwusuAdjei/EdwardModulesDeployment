from moduleA.main import add


def test_add():
    assert add(2, 2) == 4
    assert add(-2, 2) == 0
    assert add(0, 0) == 0


