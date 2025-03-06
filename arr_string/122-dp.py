class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold , unhold = -prices[0] , 0

        for i in range(1, len(prices)):
            hold = max(hold, unhold-prices[i])
            unhold = max(prices[i]+hold, unhold)

        return unhold