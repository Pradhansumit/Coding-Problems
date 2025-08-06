from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        allocated = 0
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    allocated += 1
                    baskets[j] = -1
                    break
        return n - allocated

sol = Solution()
print(sol.numOfUnplacedFruits([4,2,5],[3,5,4]))
