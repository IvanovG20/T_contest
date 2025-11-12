def main(n: int, heights: list[int]):
    wrong_even = []  # четные на четных
    wrong_odd = []  # нечетные на нечетных

    for i in range(n):
        if i % 2 == 0:
            if heights[i] % 2 == 0:
                wrong_even.append(i+1)
        else:
            if heights[i] % 2 == 1:
                wrong_odd.append(i+1)

    if not wrong_even and not wrong_odd:
        odd_numbers = []
        even_numbers = []
        for i in range(n):
            if heights[i] % 2 == 1:
                odd_numbers.append(i+1)
            else:
                even_numbers.append(i+1)

        if len(odd_numbers) >= 2:
            return f"{odd_numbers[0]} {odd_numbers[1]}"
        elif len(even_numbers) >= 2:
            return f"{even_numbers[0]} {even_numbers[1]}"
        else:
            return '-1 -1'
    elif len(wrong_even) == 1 and len(wrong_odd) == 1:
        return f'{wrong_odd[0]} {wrong_odd[1]}'
    else:
        return '-1 -1'


n = int(input())
if not 2 <= n <= 1000:
    raise ValueError
a = list(map(int, input().split()))
if not 1 <= len(a) <= 10**9:
    raise ValueError
print(main(n, a))
