class Solution:
    def maxArea(self, height: List[int]) -> int:

        L, R = 0, len(height) - 1

        # max container will be the maximum area found
        # height will be the smaller of the two pointers
        # width will be the difference in array positions from the right and left pointer

        area = 0

        while L < R:
            maxH = max(height[L], height[R])
            minH = min(height[L], height[R])
            runningCount = (R - L) * (minH)

            if minH == height[L]:
                L += 1
            else:
                R -= 1
            if runningCount > area:
                area = runningCount

        return area
