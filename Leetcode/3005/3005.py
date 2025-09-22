from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # BY USING COUNTER AND SORTING IN DESC ORDER OF VALUES

        # ans: int = 0
        # maxm: int = 0
        # counts = Counter(nums)

        # # SORT THE FUNCTION BASED ON THE VALUES IN DESC ORDER
        # counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        # for k, v in counts.items():
        #     if v >= maxm:
        #         maxm = v
        #         ans += v

        # return ans

        # BY SIMPLY FINDING THE MAX VALUES AMONG THE HASH TABLE VALUES

        counts = Counter(nums)
        maxm = max(counts.values())
        ans: int = 0
        for n in set(nums):
            if counts[n] == maxm:
                ans += counts[n]
        return ans


sol = Solution()
print(sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
print(sol.maxFrequencyElements([1, 2, 3, 4, 5]))
