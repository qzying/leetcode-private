# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_l, pre_r, inorder, in_l, in_r):
        if pre_l > pre_r:
            return None
        root_val = preorder[pre_l]
        root_idx = inorder.index(root_val)
        left = root_idx - in_l
        root = TreeNode(val=root_val)
        root.left = self.build(
            preorder, pre_l + 1, pre_l + left, inorder, in_l, root_idx - 1
        )
        root.right = self.build(
            preorder, pre_l + left + 1, pre_r, inorder, root_idx + 1, in_r
        )
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root_val = preorder.pop(0)
            root_idx = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder, inorder[:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx + 1 :])
            return root
