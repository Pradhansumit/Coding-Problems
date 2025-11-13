class Solution:
    def maxOperations(self, s: str) -> int:
        res: int = 0
        ones: int = 0

        for i, c in enumerate(s):
            if s[i] == "1":
                ones += 1
            elif i > 0 and s[i - 1] == "1":
                res += ones

        return res


sol = Solution()
print(sol.maxOperations("1001101"))
print(sol.maxOperations("00111"))
