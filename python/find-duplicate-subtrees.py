r"""
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

下面是两个重复的子树：

      2
     /
    4
和

    4

因此，你需要以列表的形式返回上述重复子树的根结点。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        nodes = collections.defaultdict(list)

        def helper(root):
            if not root:
                return '#'
            struct = ','.join([str(root.val), helper(root.left), helper(root.right)])
            nodes[struct].append(root)
            return struct

        helper(root)
        return [v[0] for v in nodes.values() if len(v) > 1]
