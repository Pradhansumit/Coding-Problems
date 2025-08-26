from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        left: int = 0
        right: int = 0
        ans: int = 0

        while right < len(s):
            seen[s[right]] = seen.get(s[right], 0) + 1
            while right - left + 1 - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
