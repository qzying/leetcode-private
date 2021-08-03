r"""
给定一个二进制数组，计算其中最大连续1的个数。

示例：

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续1，所以最大连续1的个数是3.
 
提示：
(1) 输入的数组只包含0和1。
(2) 输入数组的长度是正整数，且不超过10,000。
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, tmp = 0, 0
        for x in nums:
            if x == 1:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 0
        return max(res, tmp)
