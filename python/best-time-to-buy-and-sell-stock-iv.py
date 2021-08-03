r"""
给定一个整数数组prices，它的第i个元素prices[i]是一支给定的股票在第i天的价格。
设计一个算法来计算你所能获取的最大利润，你最多可以完成k笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第1天(股票价格 = 2)的时候买入，在第2天(股票价格 = 4)的时候卖出，这笔交易所能获得利润 = 4-2 = 2。

示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第2天(股票价格 = 2)的时候买入，在第3天(股票价格 = 6)的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第5天(股票价格 = 0)的时候买入，在第6天(股票价格 = 3)的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 
提示：
(1) 0 <= k <= 100
(2) 0 <= prices.length <= 1000
(3) 0 <= prices[i] <= 1000
"""
import numpy as np


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = np.zeros((n + 1, k + 1, 2))
        dp[0, :, 0] = 0
        dp[0, :, 1] = -sys.maxsize
        dp[:, 0, 0] = 0
        dp[:, 0, 1] = -sys.maxsize
        for i in range(1, n + 1):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
        return int(dp[n][k][0])
