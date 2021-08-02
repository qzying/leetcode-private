r"""
给你一棵二叉树的根节点root，请你返回层数最深的叶子节点的和。

示例 1：

        1
       / \
      2   3
     /  \   \
    4    5   6
   /          \
  7            8

输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15

示例 2：

输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19
 
提示：
(1) 树中节点数目在范围 [1, 104] 之间。
(2) 1 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
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
                res = tmp
                tmp = []
                one = []
            for x in two:
                tmp.append(x.val)
                if x.left:
                    one.append(x.left)
                if x.right:
                    one.append(x.right)
            if tmp:
                res = tmp
                tmp = []
                two = []
        return sum(res)
