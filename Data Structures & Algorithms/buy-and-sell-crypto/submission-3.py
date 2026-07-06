class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                current_profit = prices[i] - min_price
                if max_profit < current_profit:
                    max_profit = current_profit

        return max_profit
        
