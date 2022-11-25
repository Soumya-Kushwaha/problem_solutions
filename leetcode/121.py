class Solution:
    def maxProfit(self, prices):
        buy = 0
        max_profit = 0
        for sell in range(1, len(prices)):
            currentProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(currentProfit, max_profit)
            else:
                buy = sell
        return max_profit
