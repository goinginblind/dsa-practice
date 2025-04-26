def maxProfit(prices: list[int]) -> int:
    # 1. Make prices[0] the minimum and maximum at the moment
    if len(prices) <= 1:
        return 0
    curr_min_index, curr_max_index = 0, 0
    alltime_max = prices[curr_max_index] - prices[curr_min_index]
    curr_max = alltime_max

    # 2. Go through the prices
    for index in range(1, len(prices)):
        # 2.1. If the current_price is higher than current maximum, update current maximum
        if prices[index] > prices[curr_max_index]:
            curr_max_index = index 
            curr_max = prices[curr_max_index] - prices[curr_min_index]
        
        # 2.2. If the current_price is lower than current minimum, assign new current_min_ind, current_max_ind and set current max to 0
        if prices[index] < prices[curr_min_index]:
            curr_min_index, curr_max_index = index, index
            curr_max = 0
        alltime_max = max(curr_max, alltime_max)
    return alltime_max




def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))


if __name__ == '__main__':
    main()