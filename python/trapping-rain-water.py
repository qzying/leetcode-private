r"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining. 

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
  
    ^                                             
    |                                             
  3 |                       +--+                  
    |                       |  |                  
  2 |          +--+xxxxxxxxx|  +--+xx+--+         
    |          |  |xxxxxxxxx|  |  |xx|  |         
  1 |   +--+xxx|  +--+xxx+--+  |  +--+  +--+      
    |   |  |xxx|  |  |xxx|  |  |  |  |  |  |      
  0 +---+--+---+--+--+---+--+--+--+--+--+--+----->
      0  1   0  2  1   0  1  3  2  1  2  1        

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0
        l, r = 0, n-1
        max_l, max_r = height[l], height[r]
        res = 0
        while l < r:
            if max_l < max_r:
                res += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        return res