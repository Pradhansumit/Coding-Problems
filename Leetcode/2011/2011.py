from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res: int = 0
        for op in operations:
            if op == "--X" or op == "X--":
                res -= 1
            else:
                res += 1
        return res


sol = Solution()
print(sol.finalValueAfterOperations(["--X", "X++", "X++"]))
print(sol.finalValueAfterOperations(["++X", "++X", "X++"]))
print(sol.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
