class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            _bin = bin(n)
            _bin = str(_bin)[2:]
            set_bin = set(_bin)
            if len(set_bin) == 1 and set_bin == {"1"}:
                return n
            n += 1


sol = Solution()
print(sol.smallestNumber(5))
print(sol.smallestNumber(10))
print(sol.smallestNumber(3))
