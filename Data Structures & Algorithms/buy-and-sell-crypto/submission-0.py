class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        best_i, best_j = -1, -1
        best_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > best_profit:
                    best_profit = prices[j] - prices[i]
                    best_i = i 
                    best_j = j

        if best_i == -1:
            return 0
        return best_profit
        
