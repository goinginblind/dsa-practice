def guessNumber(n: int) -> int:
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        if result == -1:
            right = mid - 1
        if result == 1:
            left = mid + 1
