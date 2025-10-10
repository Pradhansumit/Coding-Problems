from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")

        for i in range(len(energy)):
            j = i + k
            count = energy[i]
            while j < len(energy):
                count += energy[j]
                j += k
            ans = max(ans, count)

        return ans


sol = Solution()
print(sol.maximumEnergy([5, 2, -10, -5, 1], 3))
print(sol.maximumEnergy([-2, -3, -1], 2))
