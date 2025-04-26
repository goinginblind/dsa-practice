import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

knapsack = [0] * (M + 1)

for i in range(N):
    weight, value = weights[i], values[i]
    for j in range(M, weight - 1, -1):
        knapsack[j] = max(knapsack[j], knapsack[j - weight] + value)

print(knapsack[M])

# 3 10
# 1 7 5