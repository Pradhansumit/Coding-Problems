from typing import List
from math import sqrt


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        maxm = 0

        for l, w in dimensions:
            diagonal = sqrt(l * l + w * w)
            if diagonal > maxm:
                maxm = max(maxm, diagonal)
                res = l * w
            elif diagonal == maxm:
                res = max(res, l * w)
        return res


sol = Solution()
print(sol.areaOfMaxDiagonal([[9, 3], [8, 6]]))
print(sol.areaOfMaxDiagonal([[3, 4], [4, 3]]))
