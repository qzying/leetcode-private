r"""
给定两个由一些闭区间组成的列表，firstList和secondList，其中firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj]。
每个区间列表都是成对不相交的，并且已经排序。返回这两个区间列表的交集 。
形式上，闭区间[a, b]（其中 a <= b）表示实数x的集合，而a <= x <= b。
两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3]和[2, 4]的交集为[2, 3] 。

示例 1：

            0   2     5      10     13           23  24 25
      A     +---+     +-------+     +-------------+  +--+
    
               1      5    8     12      15        24 25  26
      B        +------+    +------+      +----------+  +--+
    
              1  2    5    8  10         15      23 24 25
    Ans        ++     +    +--+          +--------+ +  +

输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

示例 2：

输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]

示例 3：

输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]

示例 4：

输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]

提示：
(1) 0 <= firstList.length, secondList.length <= 1000
(2) firstList.length + secondList.length >= 1
(3) 0 <= starti < endi <= 109
(4) endi < starti+1
(5) 0 <= startj < endj <= 109
(6) endj < startj+1
"""


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            if not (a1 > b2 or b1 > a2):
                res.append([max(a1, b1), min(a2, b2)])
            if a2 > b2:
                j += 1
            else:
                i += 1
        return res
