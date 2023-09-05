from hello import add, sub

def test_add():
    assert 4 == add(2,2)

def test_sub():
    assert 2 == sub(4,2)
