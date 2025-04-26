def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for asteroid in asteroids:
        # If no stack or if both move right or if previous moves left
        if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0):
            stack.append(asteroid)
            continue
        # If prev moves to the right and new one moves left
        while stack:
            if stack[-1] == abs(asteroid):
                stack.pop()
                break
            elif stack[-1] > abs(asteroid):
                break
            else:
                stack.pop()
                if not stack:
                    stack.append(asteroid)
                    break    
    return stack



def main():
    ast = [-2,2,1,-2]
    print(asteroidCollision(ast))

main()
