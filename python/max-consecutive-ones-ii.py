r"""
给定一个二进制数组，你可以最多将1个0翻转为1，找出其中最大连续1的个数。

示例 1：

输入：[1,0,1,1,0]
输出：4
解释：翻转第一个0可以得到最长的连续1，当翻转以后，最大连续1的个数为4。

注：
输入数组只包含0和1.
输入数组的长度为正整数，且不超过10,000

进阶：如果输入的数字是作为无限流逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字，您可以有效地解决吗？
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        match, res = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                match += 1
            r += 1
            while match > 1:
                if nums[l] == 0:
                    match -= 1
                l += 1
            res = max(res, r - l)
        return res
