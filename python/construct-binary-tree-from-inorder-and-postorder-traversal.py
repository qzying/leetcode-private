# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(
            inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1
        )

    def build(self, inorder, in_l, in_r, postorder, post_l, post_r):
        if in_l > in_r:
            return None
        root_val = postorder[post_r]
        root_idx = inorder.index(root_val)
        left = root_idx - in_l
        root = TreeNode(val=root_val)
        root.left = self.build(
            inorder, in_l, root_idx - 1, postorder, post_l, post_l + left - 1
        )
        root.right = self.build(
            inorder, root_idx + 1, in_r, postorder, post_l + left, post_r - 1
        )
        return root


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root_val = postorder.pop()
            root_idx = inorder.index(root_val)
            root = TreeNode(root_val)
            root.right = self.buildTree(inorder[root_idx + 1 :], postorder)
            root.left = self.buildTree(inorder[:root_idx], postorder)
            return root
