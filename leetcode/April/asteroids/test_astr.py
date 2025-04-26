import pytest
from astr3 import asteroidCollision

@pytest.mark.parametrize("asteroids, expected", [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),
    ([3, 5, -10], [-10]),
    ([1, -2, -2, -2], [-2, -2, -2]),
    ([10, -1, -2, -3, -4], [10]),
    ([-1, -2, -3], [-1, -2, -3]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, -1, 2, -2, 3, -3], [])
])
def test_asteroid_collision(asteroids, expected):
    assert asteroidCollision(asteroids) == expected