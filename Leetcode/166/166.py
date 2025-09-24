# FRACTION TO RECURRING DECIMAL


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # REQUIRED ANS IS IN STRING
        fraction: str = str(numerator / denominator)

        # FOR CHECKING THE DECIMAL PART IS REPEATING
        frac_list = fraction.split(".")

        # IF THE NUMBER IS WHOLE. EG., 2.0
        if frac_list[1] == "0":
            return frac_list[0]

        if len(frac_list[1]) > 10:
            pass

        return fraction


sol = Solution()
print(sol.fractionToDecimal(1, 2))
print(sol.fractionToDecimal(2, 1))
print(sol.fractionToDecimal(4, 333))
