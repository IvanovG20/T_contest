def solve_simple():
    n, t = map(int, input().split())
    floors = list(map(int, input().split()))
    k = int(input()) - 1
    first = floors[0]
    last = floors[-1]
    target = floors[k]
    to_first = target - first
    to_last = last - target
    if to_first <= t or to_last <= t:
        print(last - first)
    else:
        print(min(to_first * 2 + to_last, to_last * 2 + to_first))


if __name__ == "__main__":
    solve_simple()