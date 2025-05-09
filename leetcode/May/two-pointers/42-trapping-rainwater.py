def trap(height: list[int]) -> int:
    stack = [] 
    result = 0

    for ptr, hei in enumerate(height):
        while stack and height[ptr] > height[stack[-1]]:
            bottom = stack.pop()
        
            if not stack:
                break

            left = stack[-1]
            width = ptr - left - 1
            depth = min(height[left], hei) - height[bottom]
            result += depth * width
        
        stack.append(ptr)
    return result


def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))


main()