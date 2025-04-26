import pytest
from arrR import check

def test_no_element():
    assert check([]) == True

def test_one_element():
    assert check([1]) == True

def test_two_elements():
    assert check([3, 1]) == True

def test_already_sorted():
    assert check([1, 2, 3]) == True

def test_all_same():
    assert check([1, 1, 1, 1]) == True

def test_chess():
    assert check([1, 2, 1, 2, 1, 2]) == False

def test_fail_common():
    assert check([5, 6, 7, 9, 1, 2, 8, 16]) == False

def test_fail_uncommon():
    assert check([6,10,6]) == True

def test_duplicates():
    assert check([5, 6, 7, 9, 1, 5, 8]) == False
    assert check([5, 6, 7, 9, 1, 3, 8]) == False
    assert check([5, 6, 7, 9, 1, 5, 4]) == False
    assert check([5, 6, 7, 9, 5, 1, 4]) == False
    assert check([5, 6, 7, 9, 5, 1, 5]) == False

def test_regu():
    assert check([3,4,5,1,2]) == True

def test_fail_uncommon2():
    assert check([6,10, 12, 13, 64,6]) == True

def test_retard():
    assert check([1,3,2]) == False