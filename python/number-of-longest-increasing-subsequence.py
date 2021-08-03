r"""
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是[1, 3, 4, 7]和[1, 3, 5, 7]。

示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

注意: 给定的数组长度不超过2000并且结果一定是32位有符号整数。
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        # lengths
        dp1 = [1] * n
        # counts
        dp2 = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[i] == dp1[j] + 1:
                        dp2[i] += dp2[j]
                    elif dp1[i] < dp1[j] + 1:
                        dp1[i] = dp1[j] + 1
                        dp2[i] = dp2[j]
                    else:
                        pass
        longest = max(dp1)
        return sum(c for i, c in enumerate(dp2) if dp1[i] == longest)
