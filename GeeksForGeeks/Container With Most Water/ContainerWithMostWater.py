from typing import List
from collections import defaultdict, Counter


class Solution:
    def maxWater(self, arr) -> int:
        left: int = 0
        right: int = len(arr) - 1
        res: int = 0

        while left < right:
            base: int = right - left
            height: int = min(arr[left], arr[right])

            area: int = base * height
            res = max(res, area)

            if arr[right] > arr[left]:
                left += 1
            elif arr[right] < arr[left]:
                right -= 1
            else:
                right -= 1
                left += 1

        return res


sol = Solution()
print(sol.maxWater([1, 5, 4, 3]))
print(sol.maxWater([3, 1, 2, 4, 5]))
print(sol.maxWater([2, 1, 8, 6, 4, 6, 5, 5]))
