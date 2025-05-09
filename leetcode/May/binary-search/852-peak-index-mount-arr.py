def peakIndexInMountainArray(arr: list[int]) -> int:
    left, right = 1, len(arr) - 2

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid+1]:
            left = mid + 1
        
        elif arr[mid] < arr[mid-1]:
            right = mid - 1

        else:
            return mid

def main():
    arr = [11, 12, 11, 10, 9]
    print(peakIndexInMountainArray(arr))

main()
        
