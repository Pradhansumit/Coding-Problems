from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")
        n = len(energy)

        for i in range(n - k, n):
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                ans = max(total, ans)
                j -= k

        return ans


sol = Solution()
print(sol.maximumEnergy([5, 2, -10, -5, 1], 3))
print(sol.maximumEnergy([-2, -3, -1], 2))
print(sol.maximumEnergy([-1, -2, -3, 4, -5], 3))
