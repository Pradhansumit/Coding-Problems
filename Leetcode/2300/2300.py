from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        pairs: List[int] = []
        for s in spells:
            count = 0
            for p in potions:
                if s * p >= success:
                    count += 1
            pairs.append(count)

        return pairs


sol = Solution()
print(sol.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(sol.successfulPairs([3, 1, 2], [8, 5, 8], 16))
