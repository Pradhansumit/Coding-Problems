# 976. LARGEST PERIMETER TRIANGLE

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        peri: int = 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                p = nums[i] + nums[i - 1] + nums[i - 2]
                peri = max(peri, p)
        return peri


sol = Solution()
print(sol.largestPerimeter([2, 1, 2]))
print(sol.largestPerimeter([1, 2, 1, 10]))
