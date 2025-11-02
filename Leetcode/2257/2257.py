from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        ans: int = 0
        guarded: dict = {}
        total_cells: int = m * n
        walls_lookup = set()
        for w in walls:
            walls_lookup.add(tuple(w))

        for g in guards:
            guarded[tuple(g)] = 1
        for w in walls:
            guarded[tuple(w)] = 1

        for g in guards:
            row = g[0]
            col = g[1]

            up = down = row
            left = right = col

            while left > -1:
                if (row, left) in walls_lookup:
                    break
                guarded[row, left] = 1
                left -= 1

            while right < n:
                if (row, right) in walls_lookup:
                    break
                guarded[row, right] = 1
                right += 1

            while up > -1:
                if (up, col) in walls_lookup:
                    break
                guarded[up, col] = 1
                up -= 1
            while down < m:
                if (down, col) in walls_lookup:
                    break
                guarded[down, col] = 1
                down += 1

        ans = total_cells - sum(guarded.values())
        return ans


sol = Solution()
print(sol.countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))
print(sol.countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]))
