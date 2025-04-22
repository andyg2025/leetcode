class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 1
        while i<len(arr) and arr[i]<=arr[i-1]:
            i+=1

        res = 0
        while i<len(arr):
            while i<len(arr) and arr[i]<=arr[i-1]:
                i+=1
            count = 1
            while i<len(arr) and arr[i]>arr[i-1]:
                i+=1
                count += 1
            if count == 1:
                continue
            pre = count
            while i<len(arr) and arr[i]<arr[i-1]:
                i+=1
                count += 1
            if count == pre:
                continue
            res = max(res, count)
        return res