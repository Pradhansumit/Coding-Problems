from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans: int = 0
        for arr in triangle:
            ans += min(arr)
        return ans


sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(sol.minimumTotal([[-10]]))
