import heapq

class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
    
    def addNum(self, num: int)->None:
        if not self.minheap:
            self.minheap.append(num)
        else:
            if num > self.minheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        
        if len(self.minheap) - len(self.maxheap) > 1:
            num = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -num)
        
        if len(self.maxheap) - len(self.minheap) > 1:
            num = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -num)
    
    def findMedian(self)->float:
        if len(self.maxheap) == len(self.minheap):
            return  (self.minheap[0]-self.maxheap[0])/2
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()