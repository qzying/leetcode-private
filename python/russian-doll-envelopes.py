r"""
给你一个二维整数数组envelopes，其中envelopes[i] = [wi, hi] ，表示第i个信封的宽度和高度。
当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。
 
示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为3, 组合为: [2,3] => [5,4] => [6,7]。

示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1
 
提示：
(1) 1 <= envelopes.length <= 5000
(2) envelopes[i].length == 2
(3) 1 <= wi, hi <= 104
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.lengthOfLIS(list(zip(*envelopes))[1])

    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
