# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def traverse(root):
            if not root:
                return
            traverse(root.right)
            self.total += root.val
            root.val = self.total
            traverse(root.left)

        traverse(root)
        return root
