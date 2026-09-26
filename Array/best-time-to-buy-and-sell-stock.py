class Solution:
    def stockBuySell(self, arr, n):
        min_price = float("inf")
        max_profit = 0

        for i in range(len(arr)):
            if arr[i] < min_price:
                min_price = arr[i]
            profit = arr[i] - min_price
            max_profit = max(max_profit, profit)
        return max_profit
