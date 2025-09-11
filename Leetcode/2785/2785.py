class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        temp = []
        temp2 = []
        for i in range(len(s)):
            if s[i] in vowel:
                temp.append(s[i])
            else:
                temp2.append(s[i])

        temp.sort()

        x = 0
        y = 0
        res = ""
        for i in range(len(s)):
            if s[i] in vowel:
                res += temp[x]
                x += 1
            else:
                res += temp2[y]
                y += 1
        return res


sol = Solution()
print(sol.sortVowels("lEetcOde"))
print(sol.sortVowels("lYmpH"))
