class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        
        mymap = {}
        
        def dfs(i1,i2,i3):
            if (i1, i2, i3) in mymap:
                return mymap[(i1, i2, i3)]
            if i1 == len(s1) and i2==len(s2) and i3==len(s3):
                return True
            if i1<len(s1) and s3[i3]==s1[i1] and dfs(i1+1, i2, i3+1):
                return True
            if i2<len(s2) and s3[i3]==s2[i2] and dfs(i1, i2+1, i3+1):
                return True

            mymap[(i1, i2, i3)]=False
            return False

        return dfs(0,0,0)