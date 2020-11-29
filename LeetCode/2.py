# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, ll1: ListNode, ll2: ListNode) -> ListNode:
        l1 = ll1
        l2 = ll2
        if self.getLen(l1) < self.getLen(l2):
            # use l2
            carryover = 0
            prev = None
            while l2 is not None:
                l2.val = (0 if l1 is None else l1.val) + l2.val + carryover
                carryover = 0
                if l2.val >= 10:
                    l2.val -= 10
                    carryover = 1
                if l1 is not None:
                    l1 = l1.next 
                prev = l2
                l2 = l2.next
            if carryover == 1:
                prev.next = ListNode(1)
            return ll2
        else:
            # use l1
            carryover = 0
            prev = None
            while l1 is not None:
                l1.val = (0 if l2 is None else l2.val) + l1.val + carryover
                carryover = 0
                if l1.val >= 10:
                    l1.val -= 10
                    carryover = 1
                if l2 is not None:
                    l2 = l2.next            
                prev = l1
                l1 = l1.next
            if carryover == 1:
                prev.next = ListNode(1)
            return ll1
    
    def getLen(self, n):
        count = 0
        while n is not None:
            count += 1
            n = n.next
        return count
