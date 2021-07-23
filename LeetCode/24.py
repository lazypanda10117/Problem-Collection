# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        if not cur:
            return cur

        if cur.next:
            new_head = cur.next
        else:
            new_head = cur
        
        old_cur = None
        while cur:
            if not cur.next:
                break
            new_cur = cur.next
            cur.next = new_cur.next
            new_cur.next = cur
            if old_cur:
                old_cur.next = new_cur
            old_cur = cur
            cur = cur.next
        
        return new_head