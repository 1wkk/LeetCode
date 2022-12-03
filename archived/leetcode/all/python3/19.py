# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre, cur = head, head
        for _ in range(n):
            pre = pre.next
        if pre == None:
            return head.next
        while pre.next != None:
            pre = pre.next
            cur = cur.next
        cur.next = cur.next.next
        return head
