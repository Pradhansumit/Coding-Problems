# FRACTION TO RECURRING DECIMAL


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res: list[str] = []

        # CHECK FOR SIGNS
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        # APPENDING THE INTEGER PART
        res.append(str(numerator // denominator))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)

        res.append(".")

        # FOR LAST SEEN OF REPEATING NUMBER
        seen = {}

        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)


sol = Solution()
print(sol.fractionToDecimal(1, 2))
print(sol.fractionToDecimal(2, 1))
print(sol.fractionToDecimal(4, 333))
