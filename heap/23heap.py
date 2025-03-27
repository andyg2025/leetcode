# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        index = 0
        dum = ListNode()
        cur = dum

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, index, node))
                index += 1
        
        while heap:
            val, index, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
                index += 1
        
        return dum.next
        

                

        
