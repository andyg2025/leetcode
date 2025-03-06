from typing import List

class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = 0 , 0
        cur = []
        while p1<m and p2<n:
            if nums1[p1] <  nums2[p2]:
                cur.append(nums1[p1])
                p1+=1
            else:
                cur.append(nums2[p2])
                p2+=1
        
        if p1 == m:
            while p2<n:
                cur.append(nums2[p2])
                p2+=1
        else:
            while p1<m:
                cur.append(nums1[p1])
                p1+=1
        
        nums1[:] = cur[:]
        
        return nums1
    

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    result = Solution.merge(nums1, m, nums2, n)
    print(result)

if __name__ == "__main__":
    main()