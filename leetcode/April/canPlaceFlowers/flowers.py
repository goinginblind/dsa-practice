# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# 1 <= flowerbed.length <= 2 * 10^4

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    def countPossible(flowerbed: list[int]) -> int:
        counter = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1
            else:
                return 0
            
        for i in range(len(flowerbed)):
            if i != 0 and i != len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    counter += 1
            elif i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter += 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                counter += 1
        #print(flowerbed)
        #print(counter)
        return counter
    
    possible_flowers = countPossible(flowerbed)
    return True if (n <= possible_flowers or n == 0) else False

def main():
    arr = [0, 0, 0, 0, 0, 0, 0]
    n = 1   
    print(canPlaceFlowers(arr, n))


if __name__ == "__main__":
    main()