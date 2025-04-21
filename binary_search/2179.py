from typing import List

def goodTriplets(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    map = {}
    for i in range(n):
        map[nums1[i]] = i
    for i in range(n):
        nums2[i] = map[nums2[i]]

    res = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums2[i] < nums2[j] and nums2[j] < nums2[k]:
                    res+=1
    
    return res

nums1 = [2,0,1,3]
nums2 = [0,1,2,3]

print(goodTriplets(nums1, nums2))