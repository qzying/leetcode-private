r"""
给定整数数组nums和整数k，请返回数组中第k个最大的元素。
请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

提示：
(1) 1 <= k <= nums.length <= 104
(2) -104 <= nums[i] <= 104
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    def quick_select(self, nums, l, r, index):
        m = self.random_partition(nums, l, r)
        if m == index:
            return nums[m]
        elif m < index:
            return self.quick_select(nums, m + 1, r, index)
        elif m > index:
            return self.quick_select(nums, l, m - 1, index)

    def random_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i
