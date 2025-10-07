from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans: List[int] = [0] * len(rains)
        full: list[bool] = [False] * len(rains)

        def makeDry(idx, days):
            for d in days:
                if d != 0 and full[d - 1]:
                    full[d - 1] = False
                    ans[idx] = d
                    break

        for idx, day in enumerate(rains):
            if day == 0:
                makeDry(idx, rains[idx + 1 :])
                continue
            elif full[day - 1]:
                return []
            full[day - 1] = True
            ans[idx] = -1

        return ans


sol = Solution()
print(sol.avoidFlood([1, 2, 3, 4]))
print(sol.avoidFlood([1, 2, 0, 0, 2, 1]))
print(sol.avoidFlood([1, 2, 0, 1, 2]))
