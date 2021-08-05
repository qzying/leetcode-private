r"""

Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?

Note:
You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        one, two = [], []
        one.append(root)
        while one or two:
            for i, x in enumerate(one):
                if x.left:
                    two.append(x.left)
                if x.right:
                    two.append(x.right)
                if i != len(one) - 1:
                    one[i].next = one[i + 1]
            one = []
            for i, x in enumerate(two):
                if x.left:
                    one.append(x.left)
                if x.right:
                    one.append(x.right)
                if i != len(two) - 1:
                    two[i].next = two[i + 1]
            two = []
        return root
