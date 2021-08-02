r"""
给定一个二叉树的根节点root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1:

      1            <---
    /   \
   2     3         <---
    \     \
     5     4       <---

输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例 2:

输入: [1,null,3]
输出: [1,3]

示例 3:

输入: []
输出: []

提示:
(1) 二叉树的节点个数的范围是 [0,100]
(2) -100 <= Node.val <= 100 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
                res.append(tmp[-1])
                tmp = []
                one = []
            for x in two:
                tmp.append(x.val)
                if x.left:
                    one.append(x.left)
                if x.right:
                    one.append(x.right)
            if tmp:
                res.append(tmp[-1])
                tmp = []
                two = []
        return res
