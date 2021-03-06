r"""
给定一个由若干0和1组成的数组A，我们最多可以将K个值从0变成1。
返回仅包含1的最长（连续）子数组的长度。

示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,`1`,1,1,1,1,`1`]，粗体数字从0翻转到1，最长的子数组长度为6。

示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,`1`,`1`,1,1,1,`1`,1,1,0,0,0,1,1,1,1]，粗体数字从0翻转到1，最长的子数组长度为10。
 
提示：
(1) 1 <= A.length <= 20000
(2) 0 <= K <= A.length
(3) A[i] 为 0 或 1 
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        match, res = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                match += 1
            r += 1
            while match > k:
                if nums[l] == 0:
                    match -= 1
                l += 1
            res = max(res, r - l)
        return res
