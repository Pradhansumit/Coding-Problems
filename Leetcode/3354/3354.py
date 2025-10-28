from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def simulate(start, direction):
            arr = nums[:]
            curr = start
            dir = direction

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir

                else:
                    arr[curr] -= 1
                    dir = -dir
                    curr += dir
            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):
                    ans += 1
                if simulate(i, -1):
                    ans += 1

        return ans


sol = Solution()


print(sol.countValidSelections([1, 0, 2, 0, 3]))
print(sol.countValidSelections([2, 3, 4, 0, 4, 1, 0]))
