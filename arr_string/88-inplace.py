from typing import List

class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1,p2,p = m-1,n-1,m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1-=1
            else:
                nums1[p] = nums2[p2]
                p2-=1
            p-=1
        
        if p1==0:
            nums1[:p2] = nums2[:p2]

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