from typing import List
from collections import defaultdict, Counter


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_odd: int = (n + 1) // 2
        n_even: int = n // 2

        m_odd: int = (m + 1) // 2
        m_even: int = m // 2

        return n_odd * m_even + m_odd * n_even


sol = Solution()
print(sol.flowerGame(3, 2))
print(sol.flowerGame(1, 1))
