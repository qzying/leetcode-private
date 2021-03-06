r"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
(1) num1 和 num2 的长度小于110。
(2) num1 和 num2 只包含数字 0-9。
(3) num1 和 num2 均不以零开头，除非是数字 0 本身。
(4) 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                tmp = mul + res[p2]
                res[p2] = tmp % 10
                res[p1] += tmp // 10
        res = [str(x) for x in res]
        res = ''.join(res).lstrip('0')
        return res if res else '0'
