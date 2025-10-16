from collections import defaultdict
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        ans: int = 0
        mapp = defaultdict(int)

        for i in nums:
            r = (i % value + value) % value
            mapp[r] = mapp.get(r, 0) + 1

        while True:
            r = ans % value
            if mapp[r] > 0:
                mapp[r] -= 1
                ans += 1
            else:
                return ans


sol = Solution()
print(sol.findSmallestInteger([1, -10, 7, 13, 6, 8], 5))
print(sol.findSmallestInteger([1, -10, 7, 13, 6, 8], 7))
