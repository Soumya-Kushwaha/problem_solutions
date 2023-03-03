# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        d = r = 0
        while head:
            r += 2**d * head.val
            d += 1
            head = head.next

        return r
