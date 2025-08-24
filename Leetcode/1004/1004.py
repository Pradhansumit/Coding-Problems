from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left: int = 0
        right: int = 0
        count: int = 0  # to count the number of 0s
        ans: int = 0

        while right < len(nums):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans


sol = Solution()
print(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(sol.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
