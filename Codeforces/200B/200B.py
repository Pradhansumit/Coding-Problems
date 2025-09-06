import sys


def main():
    loop = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().split(" ")))
    count = 0
    x = loop - 1
    while x > -1:
        count = count + (data[x] / 100)
        x -= 1

    print((count / loop) * 100)


if __name__ == "__main__":
    main()
