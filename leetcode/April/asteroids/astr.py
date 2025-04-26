def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for asteroid in asteroids:
        # If no stack or if both move right or if previous moves left
        if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0):
            stack.append(asteroid)
            continue
        # If prev moves to the right and new one moves left
        if stack[-1] > 0 and asteroid < 0:
            # While stack is not empty
            while stack:
                # If equeal, pop and that's it
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                # If prev is smaller, pop it, and if it was the last one, just add new one to stack. break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                    if not stack:
                        stack.append(asteroid)
                        break
                    continue
                # If prev is bigger, break
                elif stack[-1] > abs(asteroid):
                    break
    
    return stack



def main():
    ast = [-2,2,1,-2]
    print(asteroidCollision(ast))

main()
