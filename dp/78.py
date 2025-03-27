class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                arr = res[i][:]
                arr.append(num)
                res.append(arr)
        
        return res