class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans: int = 0
        while True:
            if num1 == 0 or num2 == 0:
                break
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            ans += 1

        return ans


sol = Solution()
print(sol.countOperations(2, 3))
print(sol.countOperations(10, 10))
