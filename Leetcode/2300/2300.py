import bisect
from typing import List
import math


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        pairs: List[int] = []
        potions.sort()
        potion_count = len(potions)
        for spell_power in spells:
            required_strength = math.ceil(success / spell_power)
            if required_strength > potions[-1]:
                pairs.append(0)
                continue
            index = bisect.bisect_left(potions, required_strength)
            pairs.append(potion_count - index)
        return pairs


sol = Solution()
print(sol.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(sol.successfulPairs([3, 1, 2], [8, 5, 8], 16))
