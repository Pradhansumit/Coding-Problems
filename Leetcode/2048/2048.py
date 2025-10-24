from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def checkCount(n):
            for el, vl in n.items():
                if int(el) != vl:
                    return False

            return True

        i = n + 10000000000000000
        n += 1
        while n < i:
            count = Counter(str(n))
            if checkCount(count):
                return n
            n += 1
        return 0


sol = Solution()
print(sol.nextBeautifulNumber(1))
print(sol.nextBeautifulNumber(1000))
print(sol.nextBeautifulNumber(3000))
