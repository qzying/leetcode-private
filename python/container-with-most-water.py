r"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_value = max(max_value, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_value
