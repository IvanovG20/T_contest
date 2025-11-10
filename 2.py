n = int(input())

cuts = 0
pieces = 1

while pieces < n:
    pieces *= 2
    cuts += 1

print(cuts)