from typing import List
from collections import defaultdict, deque, Counter
import pprint


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        diag = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diag[i - j].append(grid[i][j])

        for k, arr in diag.items():
            arr.sort(reverse=(k >= 0))
            diag[k] = deque(arr)

        for i in range(m):
            for j in range(n):
                grid[i][j] = diag[i - j].popleft()

        return grid


sol = Solution()
print(sol.sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]))
# print(sol.sortMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sol.sortMatrix([[0, 1], [1, 2]]))
# print(sol.sortMatrix([[1]]))
