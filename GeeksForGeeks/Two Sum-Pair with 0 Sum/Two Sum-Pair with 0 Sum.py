from collections import defaultdict


class Solution:
    def getPairs(self, arr):
        seen = set()
        pairs = set()

        for v in arr:
            if -v in seen:
                pair = tuple(sorted((v, -v)))
                pairs.add(pair)
            seen.add(v)

        return [list(p) for p in sorted(pairs)]


sol = Solution()
print(sol.getPairs([-1, 0, 1, 2, -1, -4]))
print(sol.getPairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))
print(sol.getPairs([-8, -10, -10, -10, 10, 6, 1, 10]))
