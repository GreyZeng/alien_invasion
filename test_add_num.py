from add_num import add


def test_add1():
    sum = add(1,2)
    assert sum == 3

def test_add2():
    sum = add(2,2)
    assert sum == 4

def test_add3():
    sum = add(2,3)
    assert sum == 5