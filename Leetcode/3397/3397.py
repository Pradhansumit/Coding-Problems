from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        sett = set()

        for n in nums:
            for i in range(-k, k + 1):
                x = n + (i)
                if x not in sett:
                    sett.add(x)
                    break

        return len(sett)


sol = Solution()
print(sol.maxDistinctElements([1, 2, 2, 3, 3, 4], 2))
print(sol.maxDistinctElements([4, 4, 4, 4], 1))
print(sol.maxDistinctElements([8, 7, 8, 7, 10], 1))
