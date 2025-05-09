def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack = []

    for S, V in cars:
        time = (target - S) / V
        if not stack or time > stack[-1]:
            stack.append(time)
    
    return len(stack)




def main():
    target = 12 
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(carFleet(target, position, speed))

main()


