class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ("a", "e", "i", "o", "u")
        for ch in s:
            if ch in vowels:
                return True

        return False


sol = Solution()
print(sol.doesAliceWin("leetcoder"))
print(sol.doesAliceWin("bbcd"))
