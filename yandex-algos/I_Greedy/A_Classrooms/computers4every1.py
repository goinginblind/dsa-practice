import sys
input = sys.stdin.readline
 

N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

group_needs = [(i, X[i] + 1) for i in range(N)]
rooms = [(i, Y[i]) for i in range(M)]

group_needs.sort(key=lambda stu: stu[1])
rooms.sort(key=lambda spa: spa[1])

group_ptr = room_ptr = 0
assigned = 0
result = [0] * N

while group_ptr < N and room_ptr < M:
    group_index, need = group_needs[group_ptr]
    room_index, space = rooms[room_ptr]

    if need <= space:
        assigned += 1
        group_ptr += 1
        room_ptr += 1
        result[group_index] = room_index + 1
        
    else:
        room_ptr += 1

print(assigned)
print(' '.join(map(str, result)))

