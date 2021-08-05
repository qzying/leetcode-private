r"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
 
For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
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
