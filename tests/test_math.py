import pytest
# from handler.math_handler import add
def add (params):
    result = int(params['a']) + int(params['b'])
    print("finished")
    return result
def test_math():
    params = {
        'a' : 1,
        'b' : 2
    }
    assert add(params) == 6