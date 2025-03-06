from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        step = 0
        for i in range(len(nums)):
            if nums[i] == val:
                step += 1
            else:
                nums[i-step] = nums[i] 

        return len(nums)-step