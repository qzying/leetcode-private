r"""
已知存在一个按非降序排列的整数数组nums，数组中的值不必互不相同。
在传递给函数之前，nums在预先未知的某个下标k（0 <= k < nums.length）上进行了旋转，
使数组变为[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标从0开始计数）。
例如，[0,1,2,4,4,4,5,6,6,7]在下标5处经旋转后可能变为[4,5,6,6,7,0,1,2,4,4]。
给你旋转后的数组nums和一个整数target，请你编写一个函数来判断给定的目标值是否存在于数组中。
如果nums中存在这个目标值target，则返回true，否则返回false。

示例 1：

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true

示例 2：

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
 
提示：
(1) 1 <= nums.length <= 5000
(2) -104 <= nums[i] <= 104
(3) 题目数据保证 nums 在预先未知的某个下标上进行了旋转
(4) -104 <= target <= 104
 
进阶：
这是`搜索旋转排序数组`的延伸题目，本题中的nums可能包含重复元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            m = l + (r - l) // 2
            if target == nums[m]:
                return True
            if nums[m] >= nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
