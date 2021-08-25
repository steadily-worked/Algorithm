# https://www.acmicpc.net/problem/16916
import re


def main():
    a = input()
    b = input()
    if re.search(b, a):
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
