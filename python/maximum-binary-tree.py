r"""
给定一个不含重复元素的整数数组nums。一个以此数组直接递归构建的最大二叉树定义如下：
(1) 二叉树的根是数组 nums 中的最大元素。
(2) 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
(3) 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
返回有给定数组 nums 构建的 最大二叉树。

示例1：

输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]

       6
     /   \
    3     5
     \   /
      2 0
       \
        1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, l, r):
        if l > r:
            return None
        max_value = max(nums[l : r + 1])
        max_index = nums.index(max_value)
        root = TreeNode(val=max_value)
        root.left = self.build(nums, l, max_index - 1)
        root.right = self.build(nums, max_index + 1, r)
        return root
