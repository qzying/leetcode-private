r"""
给你一个整数数组nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, l, r):
        if l >= r:
            return
        m = self.random_partition(nums, l, r)
        self.quick_sort(nums, l, m - 1)
        self.quick_sort(nums, m + 1, r)

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
