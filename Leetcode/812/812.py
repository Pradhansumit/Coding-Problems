from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxH = 0  # MAX HEIGHT
        maxHpoints = []
        maxB = 0  # MAX BASE
        maxBpoints = []

        # FINDING MAX HEIGHT
        for point in points:
            if maxH < abs(point[1]):
                maxH = abs(point[1])
                maxHpoints = point

        # FINDING BASE WITH MAX DISTANCE FROM MAX HEIGHT X-AXIS
        for point in points:
            if point[0] - maxHpoints[0] > maxB:
                maxB = point[0] - maxHpoints[0]
                maxBpoints = point

        maxH = abs(maxH - maxBpoints[1])

        area = round(0.5 * maxH * maxB, 5)

        return area


sol = Solution()
print(sol.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
print(sol.largestTriangleArea([[1, 0], [0, 0], [0, 1]]))
