class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        step = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                step += 1
            else:
                nums[i-step] = nums[i]
        
        return len(nums)-step