from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        parentfolders = [folder[0]]
        for f in folder[1:]:
            m, n = len(parentfolders[-1]), len(f)
            if m >= n or not (parentfolders[-1] == f[:m] and f[m] == "/"):
                parentfolders.append(f)

        return parentfolders


sol = Solution()
print(sol.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
