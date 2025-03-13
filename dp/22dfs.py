from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(openp, closep, s):
            if openp==closep and (openp+closep)==2*n:
                result.append(s)

            if openp<n:
                dfs(openp+1, closep, s+"(")
            
            if closep<openp:
                dfs(openp, closep+1, s+")")
        
        dfs(0,0,"")

        return result