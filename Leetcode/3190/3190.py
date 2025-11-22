from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for x in nums if x % 3 != 0)


sol = Solution()
print(sol.minimumOperations([1, 2, 3, 4]))
print(sol.minimumOperations([3, 6, 9]))
