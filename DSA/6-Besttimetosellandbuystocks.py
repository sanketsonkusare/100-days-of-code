class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit