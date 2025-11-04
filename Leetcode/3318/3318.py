from typing import List
from collections import Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans: List[int] = []
        n = len(nums)
        for i in range(n - k + 1):
            temp = nums[i : i + k]
            count = Counter(temp)
            count = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
            ans.append(sum([x * y for x, y in count[:x]]))
        return ans


sol = Solution()
print(sol.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))
print(sol.findXSum([3, 8, 7, 8, 7, 5], 2, 2))
