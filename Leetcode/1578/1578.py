from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans: int = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                ans += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return ans


sol = Solution()
print(sol.minCost("abaac", [1, 2, 3, 4, 5]))
print(sol.minCost("abc", [1, 2, 3]))
print(sol.minCost("aabaa", [1, 2, 3, 4, 1]))
