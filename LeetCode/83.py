# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # need to take care of some edge cases
        cur_head = head
        if cur_head:
            next_head = cur_head.next
            while next_head is not None:
                if cur_head.val == next_head.val:
                    cur_head.next = next_head.next
                    next_head = next_head.next
                else:
                    cur_head = next_head
                    next_head = next_head.next
        
        return head
