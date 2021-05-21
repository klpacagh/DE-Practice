import pytest

@pytest.mark.parameterized("x,y,z", [(10,20,200)])
def test_method(x,y,z):
    assert x == z