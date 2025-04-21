from typing import List

# def findPeakElement(nums: List[int]) -> int:
#     l,r = 0,len(nums)
#     while l<r:
#         mid = (l+r)//2
#         if nums[mid]>nums[mid-1]:
#             l=mid+1
#         else:
#             r=mid
#     return l-1

# nums = [2,3,4,3,2]
# print(findPeakElement(nums))


# # this is the official solution
# def findPeakElement(nums: List[int]) -> int:
#     l,r = 0,len(nums)-1
    
#     while l<r:
#         mid = (l+r)//2
#         if nums[mid+1] > nums[mid]:
#             l = mid+1
#         else:
#             r=mid
#     return l
    

# nums = [2,3,4,3,2]
# print(findPeakElement(nums))

# something you need to konw
# 1. len(nums) or len(nums)-1, what is the difference between them
# 2. nums[mid]>nums[mid-1] or nums[mid+1]>nums[mid]

def find(nums):
    l,r=0,len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid+1] > nums[mid]:
            # here, is that mid could be 0?
            # yes, it is possible, when l,r = 0,1, mid=0
            # then, could mid be the len(nums)-1, the last elements?
            # yes, it is also possible, when len(nums)==0
            # but, if the r = len(nums)-1, then it is ok, because when len(nums)=1, then l,r=0,0 and the while loop won't start
            # Then, what would happend when the above condition is true?
            l = mid+1
        else:
            r = mid
    return r
# yes, this is exectly the offical solution, every thing is the best choise

# then, what to do if nums[i] could eaque to nums[i + 1]
# fisrt choise: find the former and the next element not nums[i], to see if they are bigger than it
# if former, r=mid
# if next, l=mid
# if both, each one is ok
# if none, the news[i] is the peak, ofcause, the peak is a array, contain list of same value elements

def helper(nums, mid):
    pre, next= mid-1, mid+1
    while pre>-1 and nums[pre]==nums[mid]:
        pre-=1
    while next<len(nums) and nums[next]==nums[mid]:
        next+=1
    return (pre, next)

def find(nums):
    l,r=0, len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid+1]>nums[mid]:
            l=mid+1
        elif nums[mid+1]<nums[mid]:
            r=mid
        else:
            pre, next=helper(nums, mid)
            if (pre==-1 and next==len(nums) or
                nums[pre]<nums[mid] and nums[next]<nums[mid]):
                return nums[pre+1:next]