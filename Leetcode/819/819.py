from collections import defaultdict
import operator
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        string = "".join([w.lower() if w.isalnum() else " " for w in paragraph])

        words = string.split()
        mapp = defaultdict(int)
        banned = set(banned)

        for w in words:
            if w not in banned:
                mapp[w] += 1

        return max(mapp.items(), key=operator.itemgetter(1))[0]
