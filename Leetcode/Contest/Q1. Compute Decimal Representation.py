from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # s = str(n)
        # ans: List[int] = []
        # for i in range(len(s)):
        #     rem = n % 10
        #     if rem == 0:
        #         continue
        #     ans.append(rem * 10**i)

        #     n = n // 10
        # ans.sort(reverse=True)
        # return ans

        s = str(n)
        ans = []
        for i in range(len(s)):
            x = int(int(s[i]) * (10 ** (len(s) - i - 1)))
            if x == 0:
                continue
            else:
                ans.append(x)
        return ans


sol = Solution()
print(sol.decimalRepresentation(102))
print(sol.decimalRepresentation(537))
