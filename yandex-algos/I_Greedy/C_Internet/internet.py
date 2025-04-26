import sys
input = sys.stdin.readline

target = int(input())
price_list = list(map(int, input().split()))

# Preprocess
for i in range(1, 31):
    price_list[i] = min(price_list[i], 2 * price_list[i - 1])

res = float('inf')
cost = 0
total_time = 0

for i in reversed(range(31)):
    if (target >> i) & 1:
        cost += price_list[i]
        total_time += (1 << i)
    else:
        # Try buying extra card of this size just (maybe it helps?)
        res = min(res, cost + price_list[i])

res = min(res, cost)
print(res)