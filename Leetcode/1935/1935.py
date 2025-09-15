from typing import List


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count: int = 0
        textlist: List[str] = text.strip().split(" ")
        brokenset: set = set(brokenLetters)

        for text in textlist:
            valid: bool = True
            for ch in text:
                if ch in brokenset:
                    valid = False
                    break
            if valid:
                count += 1
            else:
                continue
        return count


sol = Solution()
print(sol.canBeTypedWords("hello world", "ad"))
print(sol.canBeTypedWords("leet code", "lt"))
print(sol.canBeTypedWords("leet code", "e"))
