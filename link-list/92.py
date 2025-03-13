# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head

        dum = ListNode()
        dum.next = head

        prev = dum
        
        for _ in range(left-1):
            prev = prev.next
        
        cur = prev.next
        for _ in range(left, right):
            tem = cur.next
            cur.next = tem.next
            tem.next = prev.next
            prev.next = tem
        
        return dum.next