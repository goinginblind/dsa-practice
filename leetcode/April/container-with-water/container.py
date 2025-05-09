def maxArea(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    result = 0

    while left < right:
        result = max(result, min(heights[left], heights[right]) * (right - left))
        if heights[left] <= heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        
    return result




def main():
    height = [0,0]
    print(maxArea(height))


main()