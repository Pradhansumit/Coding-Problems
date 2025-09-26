from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    x, y, z = nums[i], nums[j], nums[k]
                    if (x + y > z) and (x + z > y) and (y + z > x):
                        res += 1
        return res


sol = Solution()
print(sol.triangleNumber([2, 2, 3, 4]))
print(sol.triangleNumber([4, 2, 3, 4]))
