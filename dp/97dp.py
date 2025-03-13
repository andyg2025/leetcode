class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        
        dp = set()
        dp.add((-1,-1))

        for i in range(1, len(s3)+1):
            new_dp = set()
            for (i1, i2) in dp:
                if (i1+1)<len(s1) and s3[i-1] == s1[i1+1]:
                    new_dp.add((i1+1, i2))
                if (i2+1)<len(s2) and s3[i-1] == s2[i2+1]:
                    new_dp.add((i1, i2+1))
            if not new_dp:
                return False
            
            dp = new_dp
        
        return True if dp else False