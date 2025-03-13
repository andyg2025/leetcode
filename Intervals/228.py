from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        l, r = 0, 0
        result = []
        while r<len(nums)-1:
            if nums[r+1] > nums[r]+1:
                if l==r:
                    result.append(str(nums[r]))
                else:
                    result.append(f'{nums[l]}->{nums[r]}')
                l=r+1
                r=r+1
            else:
                r+=1
        
        if l==r:
            result.append(str(nums[r]))
        else:
            result.append(f'{nums[l]}->{nums[r]}')

        return result
    

def main():
    s = Solution()
    nums = [0,2,3,4,6,8,9]
    print(s.summaryRanges(nums))


if __name__ ==  "__main__":
    main()