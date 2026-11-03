class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        ans = 0

        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1

            if area > ans:
                ans = area

        return ans