from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2

        return original


sol = Solution()
print(sol.findFinalValue([5, 3, 6, 1, 12], 3))
print(sol.findFinalValue([2, 7, 9], 4))
