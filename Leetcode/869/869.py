class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sortedn = "".join(sorted(str(n)))
        for i in range(32):
            val = str(2**i)
            sortedval = "".join(sorted(val))
            if sortedval == sortedn:
                return True
        return False