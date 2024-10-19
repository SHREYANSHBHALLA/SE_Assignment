# tests/test.py


def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


# Ensure there's a newline at the end of this file.
