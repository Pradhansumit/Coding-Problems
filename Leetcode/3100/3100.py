class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            newBottles = 1
            empty -= numExchange
            drunk += newBottles
            empty += newBottles

            numExchange += 1

        return drunk


sol = Solution()
print(sol.maxBottlesDrunk(13, 6))
print(sol.maxBottlesDrunk(10, 3))
