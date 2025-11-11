from collections import Counter
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros = m
        ones = n
        ans = 0
        for s in strs:
            c = Counter(s)
            if c["1"] > ones or c["0"] > zeros:
                continue

            zeros -= c["0"]
            ones -= c["1"]
            ans += 1

        return ans


sol = Solution()
print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
print(sol.findMaxForm(["10", "0", "1"], 1, 1))
