# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        profit = 0
        haveStock = False
        n = len(prices)
        while i + 1 < n:
            if prices[i] < prices[i+1] and not haveStock:
                profit -= prices[i]
                haveStock = True
            if prices[i] > prices[i+1] and haveStock:
                profit += prices[i]
                haveStock = False
            i += 1

        if haveStock:
            profit += prices[n-1]

        return profit
