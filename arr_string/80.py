from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        step = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] ==  nums[i-1] and count==1:
                step += 1
            elif nums[i] ==  nums[i-1] and count==0:
                count += 1
                nums[i-step] = nums[i]
            else:
                nums[i-step] = nums[i]
