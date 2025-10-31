from typing import List


from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for elem, val in count.items():
            if val > 1:
                res.append(elem)
        return res
