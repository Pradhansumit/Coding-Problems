from typing import List
from collections import defaultdict, Counter


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) < abs(y - z):
            return 1
        elif abs(x - z) > abs(y - z):
            return 2
        else:
            return 0


sol = Solution()
print(sol.findClosest(2, 7, 4))
print(sol.findClosest(2, 5, 6))
print(sol.findClosest(1, 5, 3))
