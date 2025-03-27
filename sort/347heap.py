import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num]+=1

        heap = []

        for key in map:
            if len(heap)<k:
                heapq.heappush(heap, (map[key], key))
                continue
            if heap[0][0] < map[key]:
                heapq.heappushpop(heap, (map[key], key))
        
        return [x[0] for x in heap]
            

