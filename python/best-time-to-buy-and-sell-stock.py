r"""
给定一个数组prices，它的第i个元素prices[i]表示一支给定股票第i天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。
设计一个算法来计算你所能获取的最大利润，如果你不能获取任何利润，返回0。

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第2天（股票价格 = 1）的时候买入，在第5天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为0。
 
提示：
(1) 1 <= prices.length <= 105
(2) 0 <= prices[i] <= 104
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        if not prices: return 0
        res = 0
        min_price = prices[0]
        for x in prices:
            if x < min_price:
                min_price = x
            else:
                res = max(res, x - min_price)
        return res
        '''
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -sys.maxsize
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0
