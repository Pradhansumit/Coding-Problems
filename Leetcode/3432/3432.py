from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        pre = 0
        count = 0
        for i in range(len(nums) - 1):
            pre += nums[i]
            total -= nums[i]
            if (pre - total) % 2 == 0:
                count += 1
        return count


sol = Solution()
print(sol.countPartitions([10, 10, 3, 7, 6]))
print(sol.countPartitions([1, 2, 2]))
