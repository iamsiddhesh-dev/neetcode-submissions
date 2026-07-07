class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            current_max_profit = float('-inf')
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    current_max_profit = max(current_max_profit, profit)
            max_profit = max(current_max_profit, max_profit)
        return max_profit