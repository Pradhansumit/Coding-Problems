from collections import defaultdict


class Spreadsheet:
    def __init__(self, rows: int):
        self.data = defaultdict(int)
        self.row = rows

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        self.data[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]  # remove leading "="
        left, right = formula.split("+")

        def get_operand_value(op: str) -> int:
            if op[0].isalpha():
                row_num = int(op[1:])
                if row_num > self.row:
                    return 0

                return self.data.get(op, 0)

            else:
                return int(op)

        return get_operand_value(left) + get_operand_value(right)
