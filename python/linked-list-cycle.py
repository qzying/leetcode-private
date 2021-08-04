r"""
Given a linked list, determine if it has a cycle in it.
Follow up: Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        return True
