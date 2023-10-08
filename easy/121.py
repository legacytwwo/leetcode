def maxProfit(prices: list[int]) -> int:
    len_array = len(prices)
    max = 0
    i = 0

    for j in range(1, len_array):
        if prices[i] > prices[j]:
            i = j
        else:
            profit = prices[j] - prices[i]
            if profit > max: max = profit
    return max



assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0