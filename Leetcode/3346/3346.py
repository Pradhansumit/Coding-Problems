from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        lookup: set = set(nums)

        for i in range(len(nums)):
            for op in range(-k, k + 1):
                operate: int = nums[i] + op
                if numOperations and operate in lookup:
                    nums[i] = operate
                    # numOperations -= 1

        mapp = Counter(nums)
        mapp = sorted(mapp.items(), key=lambda item: item[1])
        print(mapp)
        return mapp[-1][1]


sol = Solution()

print(sol.maxFrequency([1, 4, 5], 1, 2))
print(sol.maxFrequency([5, 11, 20, 20], 5, 1))
