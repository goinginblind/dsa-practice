def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    result = []
    max_candies = max(candies)

    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result


def main():
    candies = [2,3,5,1,3]
    extraCandies = 3

    print(kidsWithCandies(candies, extraCandies))

main()