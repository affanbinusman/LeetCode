class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l<r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            elif height[l] < height[l+1]:
                l += 1
            else:
                r -= 1
        
        return res