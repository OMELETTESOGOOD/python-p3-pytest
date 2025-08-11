from lib.not_none_functions import return_not_none

def test_return_not_none():
    '''return_not_none() should not return None'''
    result = return_not_none()
    assert result is not None

