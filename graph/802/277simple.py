# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        cele = 0
        for i in range(n):
            if knows(cele, i):
                cele = i
        
        for i in range(n):
            if i==cele:
                continue
            if knows(cele, i) or not knows(i, cele):
                return -1
        
        return cele