from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        ans = float("inf")

        def checkInc(n):
            for i in range(len(n) - 1):
                if n[i] > n[i + 1]:
                    return False
            return True

        def checkDec(n):
            for i in range(len(n) - 1):
                if n[i] < n[i + 1]:
                    return False
            return True

        for i in range(1, len(nums)):
            left, right = (nums[:i], nums[i:])

            if not checkInc(left) or not checkDec(right):
                continue
            ans = min(ans, abs(sum(left) - sum(right)))

        if ans == float("inf"):
            return -1
        else:
            return ans


sol = Solution()
print(sol.splitArray([1, 3, 2]))
print(sol.splitArray([1, 2, 4, 3]))
print(sol.splitArray([3, 1, 2]))
