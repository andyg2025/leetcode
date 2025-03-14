class Solution:
    def trap(self, height: List[int]) -> int:
        last = 0
        result = 0
        for i in range(len(height)):
            if height[i] > height[last]:
                for j in range(last, i):
                    result += (height[last]-height[j])
                last = i

        last = len(height)-1
        for i in range(len(height)-1, -1, -1):
            if height[i] >= height[last]:
                for j in range(i+1, last):
                    result += (height[last]-height[j])
                    print(result)
                last = i
        
        return result