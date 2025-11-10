def main(l, r):
    count = 0
    max_len = len(str(r))
    for lenght in range(1, max_len+1):
        for i in range(1, 10):
            num = int(str(i)*lenght)
            if l <= num <= r:
                count += 1
            elif num > r:
                break
    return count


l, r = map(int, input().split())
print(main(l, r))