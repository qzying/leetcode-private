r"""
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。

示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是"b"，所以其长度为1。

示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

示例 4:

输入: s = ""
输出: 0
 
提示：
(1) 0 <= s.length <= 5 * 104
(2) s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        win = collections.defaultdict(int)
        while r < len(s):
            val = s[r]
            win[val] += 1
            r += 1
            while win[val] > 1:
                win[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res
