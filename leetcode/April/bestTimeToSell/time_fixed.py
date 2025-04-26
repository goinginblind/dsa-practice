def maxProfit(prices: list[int]) -> int:
    # 1. Make 0 the minimum and maximum at the moment, alltime high is 0 too
    lowest_in_window, highest_in_window, alltime_max = 0, 0, 0
    max_diff_in_window = alltime_max

    # 2. Go through the prices
    for current in range(0, len(prices)):
        
        # 2.1. If the current_price is higher than current window maximum, update current window maximum
        if prices[current] > prices[highest_in_window]:
            highest_in_window = current 
            max_diff_in_window = prices[highest_in_window] - prices[lowest_in_window]
        
        # 2.2. If the current_price is lower than window's minimum, then start a new window
        if prices[current] < prices[lowest_in_window]:
            lowest_in_window, highest_in_window = current, current
            max_diff_in_window = 0

        # 2.3 Check if current windows maximum diff is greater than alltime high difference
        alltime_max = max(max_diff_in_window, alltime_max)
    
    # 3. Return alltime_max
    return alltime_max




def main():
    prices = [4, 2, 9, 1, 10] 
    print(maxProfit(prices))


if __name__ == '__main__':
    main()