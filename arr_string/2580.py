class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 1000000000+7
        
        ranges.sort()
        
        count = 0
        last_end = 0

        for r in ranges:
            if count == 0:
                count = 1
                last_end = r[1]
                continue
            
            if r[0] <= last_end:
                last_end = max(last_end, r[1])
            else:
                count += 1
                last_end = r[1]
        
        return (2**count)%mod