class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        # FINDING MAX LEN -> ADDING EXTRA 0'S WHERE NEEDED
        n: int = max(len(v1), len(v2))
        v1 = v1 + [0] * (n - len(v1))
        v2 = v2 + [0] * (n - len(v2))

        for i in range(n):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1

        return 0


sol = Solution()

print(sol.compareVersion("1.2", "1.10"))
print(sol.compareVersion("1.01", "1.001"))
print(sol.compareVersion("1.0", "1.0.0.0"))
