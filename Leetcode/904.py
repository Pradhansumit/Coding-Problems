from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = defaultdict(int)
        res = 0
        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res


sol = Solution()
print(sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
