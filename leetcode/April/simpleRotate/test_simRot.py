# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 23^1 - 1
# 0 <= k <= 10^5


from simRot import rotate

def test_list_1():
    assert rotate([1], 7) == [1]

def test_list_2():
    assert rotate([1, 2], 2) == [1, 2]

def test_even():
    assert rotate([1, 2, 99, 123], 2) == [99, 123, 1, 2]

def test_uneven():
    assert rotate([1, 2, 3], 2) == [2, 3, 1]

def test_k_0_list_not():
    assert rotate([1, 2, 3], 0) == [1, 2, 3]

def test_k_0_list_1():
    assert rotate([1], 0) == [1]

def test_regular():
    assert rotate([1,2,3,4,5,6,7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate([1, 2, 3, 4], 3) == [2, 3, 4, 1]