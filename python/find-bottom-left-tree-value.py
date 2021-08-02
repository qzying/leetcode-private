r"""
给定一个二叉树的根节点root，请找出该二叉树的最底层最左边节点的值。
假设二叉树中至少有一个节点。

示例 1:

     2
    / \
   1   3

输入: root = [2,1,3]
输出: 1

示例 2:

       1
      / \
     2   3
    /   / \
   4   5   6
      /
     7

输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
 
提示:
(1) 二叉树的节点个数的范围是 [1,104]
(2) -231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
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
        return res[0]
