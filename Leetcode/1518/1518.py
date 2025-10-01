class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles < numExchange:
            return numBottles

        ans: int = numBottles

        while numBottles >= numExchange:
            filledBottles = numBottles // numExchange
            emptyBottles = numBottles % numExchange
            numBottles = emptyBottles + filledBottles
            ans += filledBottles
        return ans
