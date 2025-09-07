from typing import List
from collections import defaultdict, Counter


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res: List[int] = []
        i: int = 1
        if n % 2 != 0:
            res.append(0)

        while len(res) != n:
            res.append(-i)
            res.append(i)
            i += 1

        return res


sol = Solution()
print(sol.sumZero(5))
print(sol.sumZero(3))
print(sol.sumZero(1))
