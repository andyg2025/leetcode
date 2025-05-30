class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        if n%2==0:
            return (self.arr[n//2] + self.arr[n//2-1])/2
        else:
            return self.arr[n//2]