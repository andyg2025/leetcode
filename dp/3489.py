class Solution:

    def check(self, dp):
        for sub_dp in dp:
            if not sub_dp[-1]:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        dp = [[False]*(n+1) for n in nums]
        for i in range(len(nums)):
            dp[i][0] = True
        count = 0

        if self.check(dp):
            return count

        for l, r, val in queries:
            count+=1
            for i in range(l, r+1):
                for j in range(nums[i], val-1, -1):
                    dp[i][j] = dp[i][j-val] or dp[i][j]
            if self.check(dp):
                return count
        
        return -1