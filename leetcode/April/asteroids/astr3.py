def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    i = 0
    while i < len(asteroids):
        if not stack or (stack[-1] > 0 and asteroids[i] > 0) or stack[-1] < 0:
            stack.append(asteroids[i])
            i += 1
            continue
        elif stack[-1] > abs(asteroids[i]):
            i += 1
        elif stack[-1] == abs(asteroids[i]):
            stack.pop()
            i += 1
        elif stack[-1] < abs(asteroids[i]):
            stack.pop()
    return stack

def main():
    ast = [8, -8]
    print(asteroidCollision(ast))

main()
