from typing import List
from collections import defaultdict, Counter


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if "0" in str(n - i) or "0" in str(i):
                continue
            return [i, n - i]


sol = Solution()
print(sol.getNoZeroIntegers(2))
print(sol.getNoZeroIntegers(11))
