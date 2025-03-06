from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        self.reverse(nums)
        self.reverse(nums[:k])
        self.reverse(nums[k:])

    def reverse(self, nums: List[int]):
        left, right = 0, len(nums)

        while right>left:
            nums[right], nums[left] = nums[left], nums[right]