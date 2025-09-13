from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelsCount = defaultdict(int)
        constsCount = defaultdict(int)
        maxV, maxC = 0, 0
        vowels = "aeiou"

        for ch in s:
            if ch in vowels:
                vowelsCount[ch] = vowelsCount.get(ch, 0) + 1
                maxV = max(maxV, vowelsCount[ch])
            else:
                constsCount[ch] = constsCount.get(ch, 0) + 1
                maxC = max(maxC, constsCount[ch])

        return maxV + maxC


sol = Solution()
print(sol.maxFreqSum("successes"))
print(sol.maxFreqSum("aeiaeia"))
