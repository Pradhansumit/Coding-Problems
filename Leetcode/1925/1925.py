class Solution:
    def countTriples(self, n: int) -> int:
        squares = []
        for i in range(n, 0, -1):
            squares.append(i**2)
        sett = set(squares)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if squares[i] - squares[j] in sett:
                    count += 1
        return count


sol = Solution()
print(sol.countTriples(5))
print(sol.countTriples(10))
