from typing import List
import heapq

def minMeetingRooms(intervals: List[List[int]]) -> int:
    heap = []

    intervals.sort()

    for start, end in intervals:
        if not heap or start < heap[0]:
            heapq.heappush(heap, end)
        else:
            heapq.heappushpop(heap, end)
        
    return len(heap)

intervals = [[2,15],[36,45],[9,29],[16,23],[4,9]]
print(minMeetingRooms(intervals))