r"""
给你一个字符串s，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为"bbbb"。

示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为"bb"。

提示：
(1) 1 <= s.length <= 1000
(2) s仅由小写英文字母组成
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.longestCommonSubsequence(s, s[::-1])

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
