from math import ceil

def minEatingSpeed(piles: list[int], h: int) -> int:
    biggest_pile = max(piles)
    if h == len(piles):
        return biggest_pile
    
    left, right = 1, biggest_pile

    while left < right:
        mid = (left + right) // 2
        divided = sum(ceil(pile / mid) for pile in piles)

        if divided <= h:
            right = mid
        
        elif divided > h:
            left = mid + 1 
    return right

def main():
    piles = [10**9] * 10000
    h = 10**9
    print(minEatingSpeed(piles, h))

main()
