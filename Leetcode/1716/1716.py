import math


class Solution:
    def totalMoney(self, n: int) -> int:
        rounds: int = math.ceil(n / 7)
        i: int = 1
        ans: int = 0
        while i <= rounds:
            j = i
            end: int = j + 6
            while j <= end and n > 0:
                ans += j
                j += 1
                n -= 1
            i += 1

        return ans


sol = Solution()
print(sol.totalMoney(4))
print(sol.totalMoney(10))
print(sol.totalMoney(20))
