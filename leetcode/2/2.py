from typing import Optional


class ListNode:
    def __init__(self, val, _next=None) -> None:
        self.val = val
        self.next = _next


class Solution:
    def chain(self, node: Optional[ListNode]) -> list:
        a = ""
        while node:
            a += str(node.val)
            node = node.next

        return int(a[::-1])

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = str(self.chain(l1) + self.chain(l2))
        hhead = head = ListNode(int(res[-1]))
        for i in res[-2::-1]:
            _next = ListNode(int(i))
            head.next = _next
            head = _next

        return hhead
