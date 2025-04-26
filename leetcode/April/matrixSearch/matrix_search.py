def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # Binary search for row
    top, bottom = 0, len(matrix) - 1
    while top < bottom:
        mid = (top + bottom) // 2 + 1
        if matrix[mid][0] < target:
            top = mid
        elif matrix[mid][0] > target:
            bottom = mid - 1
        elif matrix[mid][0] == target:
            return True
        
    # Binary search inside the row
    left, right = 0, len(matrix[top]) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[top][mid] == target:
            return True
        elif matrix[top][mid] < target:
            left = mid + 1
        elif matrix[top][mid] > target:
            right = mid - 1
    return False
    

def main():
    matrix = [
        [27, 29],
        [31, 68]
        ]
    target = 68

    print(searchMatrix(matrix, target))

main()