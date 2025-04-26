# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    stack = []
    
    for i in range(1,len(temperatures)):
        if temperatures[i - 1] < temperatures[i]:
            result[i - 1] = 1
        elif temperatures[i - 1] >= temperatures[i]:
            stack.append((temperatures[i - 1], i - 1))
        
        while stack and temperatures[i] > stack[-1][0]:
            result[stack[-1][1]] = i - stack[-1][1]
            stack.pop()

    return result








def main():
    temps = [73,74,75,71,69,72,76,76,73,80]
    print(dailyTemperatures(temps))


main()