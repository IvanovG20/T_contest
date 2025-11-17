def main(n, lunches):
    x = 100
    cupons = 0
    sorted_lunches = sorted(lunches, reverse=True)
    total_cost = 0

    for i in lunches:
        if i in lunches:
            if i < x:
                total_cost += i
                sorted_lunches.remove(i)
            else:
                total_cost += i
                sorted_lunches.remove(i)
                cupons += 1
        if cupons:
            max_val = max(sorted_lunches)
            sorted_lunches.remove(max_val)
            lunches.remove(max_val)
            cupons -= 1
    return total_cost

n = int(input())
lunches = []
for _ in range(n):
    lunches.append(int(input().strip()))
print(main(n, lunches))