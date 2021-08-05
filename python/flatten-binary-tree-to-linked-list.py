r"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6


Hints:
If you notice carefully in the flattened tree, each node's right child points to 
the next node of a pre-order traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right
        # root <=> left
        root.left = None
        root.right = left
        # left <=> right
        p = root
        while p.right:
            p = p.right
        p.right = right
