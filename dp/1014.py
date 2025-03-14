# Find the most bigest output for the current j
# Check if values[j]+j is bigger than values[i]+i, if so, then using j as the bigest i after.

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        i = 0
        result = 0
        for j in range(1, n):
            result = max(result, (values[i]+values[j]+i-j))
            if values[j] > values[i]+i-j:
                i = j
        
        return result