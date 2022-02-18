# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # stack solution
        # s1, s2 = [], []
        # while l1:
        #     s1.append(l1.val)
        #     l1 = l1.next
        # while l2:
        #     s2.append(l2.val)
        #     l2 = l2.next
        # ans = None
        # c = 0
        # while s1 or s2 or c != 0:
        #     a = s1.pop() if s1 else 0
        #     b = s2.pop() if s2 else 0
        #     s = a + b + c
        #     c = s // 10
        #     s %= 10
        #     node = ListNode(s)
        #     node.next = ans
        #     ans = node
        # return ans

        # reverse list
        def reverseList(head: ListNode) -> ListNode:
            # iteration
            l, r = None, head
            while r:
                rr = r.next
                r.next = l
                l = r
                r = rr
            return l

        l1 = reverseList(l1)
        l2 = reverseList(l2)
        c = 0
        ans = None
        while l1 or l2 or c != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            s = a + b + c
            c = s // 10
            s %= 10
            node = ListNode(s)
            node.next = ans
            ans = node
        return ans
