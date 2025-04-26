import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

# 1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9

    left = 0
    sequence_len = 0
    result = []

    while left < n:
        right = left
        min_in_window = a[left]

        while right < n:
            min_in_window = min(min_in_window, a[right])
            window_len = right - left + 1

            if window_len <= min_in_window:
                right += 1
            
            else:
                break
        result.append(right - left)
        left = right
    
    print(len(result))
    print(' '.join(map(str, result)))









