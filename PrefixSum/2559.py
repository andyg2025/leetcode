class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count=[0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count.append(count[-1]+1)
            else:
                count.append(count[-1])
        
        res = []
        for l,r in queries:
            res.append(count[r+1]-count[l])
        
        return res