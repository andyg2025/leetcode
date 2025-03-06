class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        # the profits that if buy in day i-1 and sale it in day i;
        # add all the positive profit tegother, is the finial result
        for i in range(1, len(prices)):
            profit = prices[i]-prices[i-1]
            if profit >0:
                result += profit

        return result