def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """ 

    left, right = 0, len(s) - 1
    mid = (len(s) - 1) // 2

    while left <= mid:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def main():
    arr = ['h', 'e', 'l', 'l', 'o']
    reverseString(arr)

    print(arr)

main()
    