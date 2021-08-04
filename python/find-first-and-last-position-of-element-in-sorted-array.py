r"""
给定一个按照升序排列的整数数组nums，和一个目标值target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值target，返回[-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 
示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 
提示：
(1) 0 <= nums.length <= 105
(2) -109 <= nums[i] <= 109
(3) nums 是一个非递减数组
(4) -109 <= target <= 109
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        l = self.lower_bound(nums, target)
        r = self.upper_bound(nums, target)
        if nums[l] != target:
            l = -1
        if nums[r] != target:
            r = -1
        return [l, r]

    def lower_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
            elif nums[m] == target:
                r = m
        return l

    def upper_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
            elif nums[m] == target:
                l = m + 1
        return l - 1
