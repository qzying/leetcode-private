r"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the 
tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is 
defined between two nodes v and w as the lowest node in T that has both v and w as 
descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
  6       _2      0        8
         /  \
        7    4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example 
is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according 
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
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        meta = {root: None}

        def traverse(node):
            if not node:
                return
            if node.left:
                meta[node.left] = node
            if node.right:
                meta[node.right] = node
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        l1, l2 = p, q
        while l1 != l2:
            l1 = meta.get(l1, q)
            l2 = meta.get(l2, p)
        return l1
