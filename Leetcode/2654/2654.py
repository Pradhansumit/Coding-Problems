from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        gcd = -1
        n = len(nums)
        for i in range(1, min(nums) + 1):
            c = 0
            for el in nums:
                if el % i == 0:
                    c += 1

            if c == n:
                gcd = i

        return len(nums) if gcd == 1 else -1


sol = Solution()
print(sol.minOperations([2, 6, 3, 4]))
print(sol.minOperations([2, 10, 6, 14]))
print(sol.minOperations([410193, 229980, 600441]))
