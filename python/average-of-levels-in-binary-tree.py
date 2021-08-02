r"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：

输入：

    3
   / \
  9  20
    /  \
   15   7

输出：[3, 14.5, 11]

解释：第0层的平均值是3,  第1层是14.5, 第2层是11。因此返回[3, 14.5, 11]。

提示：节点值的范围在32位有符号整数范围内。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res, one, two = [], [], []
        one.append(root)
        while one or two:
            tmp = []
            for x in one:
                tmp.append(x.val)
                if x.left:
                    two.append(x.left)
                if x.right:
                    two.append(x.right)
            if tmp:
                res.append(sum(tmp) / len(tmp))
                tmp = []
                one = []
            for x in two:
                tmp.append(x.val)
                if x.left:
                    one.append(x.left)
                if x.right:
                    one.append(x.right)
            if tmp:
                res.append(sum(tmp) / len(tmp))
                tmp = []
                two = []
        return res
