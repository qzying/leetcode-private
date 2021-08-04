r"""
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个 不同的元素。

示例 1：

输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

示例 2：

输入：matrix = [[-5]], k = 1
输出：-5
 
提示：
(1) n == matrix.length
(2) n == matrix[i].length
(3) 1 <= n <= 300
(4) -109 <= matrix[i][j] <= 109
(5) 题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
(6) 1 <= k <= n2
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            m = l + (r - l) // 2
            total = self.count(matrix, m)
            if total >= k:
                r = m - 1
            else:
                l = m + 1
        return l

    def count(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        i, j = 0, n - 1
        while j >= 0 and i <= m - 1:
            if matrix[i][j] <= target:
                ans += j + 1
                i += 1
            else:
                j -= 1
        return ans
