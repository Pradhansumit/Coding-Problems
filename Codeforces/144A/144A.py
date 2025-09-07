import sys
from typing import List


def main() -> None:
    x: int = int(sys.stdin.readline().strip())
    nums: List[int] = list(map(int, sys.stdin.readline().split(" ")))

    low, lowidx = float("inf"), 0
    high, highidx = float("-inf"), 0

    for idx, key in enumerate(nums):
        if key <= low:
            low = key
            lowidx = idx

    count: int = 0

    while lowidx < len(nums) - 1:
        count += 1
        nums[lowidx], nums[lowidx + 1] = nums[lowidx + 1], nums[lowidx]
        lowidx += 1

    for idx, key in enumerate(nums):
        if key > high:
            high = key
            highidx = idx

    while highidx > 0:
        count += 1
        nums[highidx], nums[highidx - 1] = nums[highidx - 1], nums[highidx]
        highidx -= 1

    print(count)


if __name__ == "__main__":
    main()
