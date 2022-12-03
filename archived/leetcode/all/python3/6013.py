# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # Violent solution or Originally modification
    def mergeNodes(self, h: Optional[ListNode]) -> Optional[ListNode]:
        _sum, a, c = 0, h, h.next
        while c:
            if c.val:
                _sum += c.val
            else:
                a.next.val = _sum
                a = a.next
                _sum = 0
            c = c.next
        a.next = None
        return h.next
