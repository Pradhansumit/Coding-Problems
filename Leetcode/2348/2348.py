from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                l = r

                while r < len(nums) and nums[r] == 0:
                    r += 1
                res += (r - l) * (r - l + 1) // 2
            r += 1

        return res
