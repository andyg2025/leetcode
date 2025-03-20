class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l,r = 0,0
        res = [0, len(s)+1]
        count = 0

        while count==k or r<len(s):
            if count < k:
                if s[r]=='1':
                    count += 1
                r+=1
            else:
                if s[l]=='1':
                    count -= 1
                l+=1

            # print(count, l, r)
            
            if count==k:
                if r-l < res[1]-res[0]:
                    res = [l,r]
                elif r-l == res[1]-res[0] and s[l:r] < s[res[0]:res[1]]:
                    res = [l,r]

        return s[res[0]:res[1]] if res[1]-res[0]<=len(s) else ''
                    