from typing import List
from collections import defaultdict, Counter


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x: int):
            low: int = 0
            high: int = len(nums)

            while low < high:
                mid: int = (low + high) // 2

                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid

            return low

        low: int = search(target)
        high: int = search(target + 1) - 1

        if low <= high:
            return [low, high]

        return [-1, -1]


sol = Solution
print(sol)
