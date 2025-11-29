from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        _sum = sum(nums)
        res = 0
        while _sum % k != 0:
            res += 1
            _sum -= 1
        return res


sol = Solution()

print(sol.minOperations([3, 9, 7], 5))
print(sol.minOperations([4, 1, 3], 4))
print(sol.minOperations([3, 2], 6))
