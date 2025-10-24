def cases(a, b):
    return a + b

def test_add():
    assert cases(2, 3) == 5      
    assert cases(-1, 1) == 0
