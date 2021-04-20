def fib(n):
    if n == 0 or n == 1:
        return n
    prev_prev = 0
    prev = 1

    for i in range(2, n+1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    #
    # prev = 0
    # current = 1
    # for i in range(2, n+1):
    #     current, prev = current + prev, current
    return current


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()
