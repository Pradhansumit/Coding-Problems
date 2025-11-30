from typing import List


# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         total = sum(nums)
#         lt, rt = 0, 0
#         length = float("inf")
#         if total % p == 0:
#             return 0
#         while rt < len(nums):
#             total -= nums[rt]
#             if total % p == 0:
#                 length = min(length, rt - lt + 1)
#                 while lt <= rt:
#                     total += nums[lt]
#                     if total % p == 0:
#                         length = min(length, rt - lt + 1)
#                     lt += 1
#             rt += 1

#         return -1 if length == float("inf") else length


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mapp = {}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            mapp[i] = total
        print(mapp)


sol = Solution()
print(sol.minSubarray([3, 1, 4, 2], 6))
print(sol.minSubarray([6, 3, 5, 2], 9))
# print(sol.minSubarray([1, 2, 3], 3))
