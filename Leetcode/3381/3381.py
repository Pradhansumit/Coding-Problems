from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        ans = float("-inf")
        add = 0

        if len(nums) == 1:
            return nums[0]

        while right < len(nums):
            add += nums[right]
            if (right - left + 1) % k == 0:
                ans = max(ans, add)
            while right == len(nums) - 1 and left < right:
                add -= nums[left]
                if (right - left + 1) % k == 0:
                    ans = max(ans, add)
                left += 1
            right += 1

        return ans


sol = Solution()
# print(sol.maxSubarraySum([1, 2], 1))
print(sol.maxSubarraySum([-1, -2, -3, -4, -5], 4))
# print(sol.maxSubarraySum([-5, 1, 2, -3, 4], 2))
# print(sol.maxSubarraySum([-8], 1))
