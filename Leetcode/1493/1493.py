from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left: int = 0
        right: int = 0
        ans: int = 0
        count: int = 0
        if 0 not in nums:
            return len(nums) - 1

        while right < len(nums):
            if nums[right] == 0:
                count += 1

            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1

            ans = max(ans, right - left)
            right += 1

        return ans


sol = Solution()
print(sol.longestSubarray([1, 1, 0, 1]))
print(sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(sol.longestSubarray([1, 1, 1]))
