r"""
给定一个整数数组，其中第i个元素代表了第i天的股票价格。​
设计一个算法计算出最大利润，在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
(1) 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
(2) 卖出股票后，你无法在第二天买入股票 (即冷冻期为1天)。

示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1, cold = 0, -sys.maxsize, 0
        for i in range(n):
            dp_i_0, dp_i_1, cold = (
                max(dp_i_0, dp_i_1 + prices[i]),
                max(dp_i_1, cold - prices[i]),
                dp_i_0,
            )
        return dp_i_0
