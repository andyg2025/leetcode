from typing import List

def countSmaller(nums: List[int]) -> List[int]:
    arr = []
    map = {}
    
    def insert(n:int)->int:
        l,r = 0, len(arr)
        while l<r:
            mid = (l+r)//2
            if arr[mid] < n:
                l = mid+1
            else:
                r = mid
            
        arr.insert(r, n)
        return map[arr[r-1]]+1 if r>0 else 0
    
    res = []
    for i in range(len(nums)-1, -1, -1):
        count = insert(nums[i])
        res.append(count)
        map[nums[i]] = count

    return res[::-1]

nums = [2,0,1]
print(countSmaller(nums))