# time complexity n log(n), n=total nodes

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            while head:
                arr.append(head.val)
                head=head.next
        
        arr.sort()
        dum = ListNode()
        cur = dum
        for val in arr:
            cur.next = ListNode(val)
            cur=cur.next
        
        return dum.next