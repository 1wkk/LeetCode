# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iteration
        # l, r = None, head
        # while r:
        #     rr = r.next
        #     r.next = l
        #     l = r
        #     r = rr
        # return l

        # recursion
        if not head or not head.next:
            return head
        rln = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rln
