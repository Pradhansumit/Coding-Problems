from typing import List
from collections import defaultdict, Counter


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n: int) -> int:
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)


sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
