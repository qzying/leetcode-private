r"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Follow up: Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        p1, p2 = head, slow
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
