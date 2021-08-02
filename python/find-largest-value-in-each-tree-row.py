r"""
给定一棵二叉树的根节点root，请找出该二叉树中每一层的最大值。

示例1：

输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:

          1
         / \
        3   2
       / \   \  
      5   3   9 

示例2：

输入: root = [1,2,3]
输出: [1,3]
解释:

          1
         / \
        2   3

示例3：

输入: root = [1]
输出: [1]

示例4：

输入: root = [1,null,2]
输出: [1,2]
解释:   

           1 
            \
             2    
 
示例5：

输入: root = []
输出: []
 
提示：
(1) 二叉树的节点个数的范围是 [0,104]
(2) -231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
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
                res.append(max(tmp))
                tmp = []
                one = []
            for x in two:
                tmp.append(x.val)
                if x.left:
                    one.append(x.left)
                if x.right:
                    one.append(x.right)
            if tmp:
                res.append(max(tmp))
                tmp = []
                two = []
        return res
