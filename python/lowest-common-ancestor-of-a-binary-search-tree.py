r"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given 
nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is 
defined between two nodes v and w as the lowest node in T that has both v and w as 
descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    __2___          ___8__
   /      \        /      \
  0       _4      7        9
         /  \
        3    5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example 
is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according 
to the LCA definition.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return root
