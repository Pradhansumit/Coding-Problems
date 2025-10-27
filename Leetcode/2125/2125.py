from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts: List[int] = [x.count("1") for x in bank]
        ans: int = 0

        counts = [x for x in counts if x != 0]
        if len(counts) == 1:
            return 0

        for i in range(0, len(counts) - 1):
            ans += counts[i] * counts[i + 1]

        return ans


sol = Solution()
print(sol.numberOfBeams(["011001", "000000", "010100", "001000"]))
print(sol.numberOfBeams(["000", "111", "000"]))
