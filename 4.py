def main(n, k, nums):
    difs = []
    for num in nums:
        for i in range(len(num)):
            new_num_str = num[:i] + '9' + num[i+1:]
            dif = int(new_num_str) - int(num)
            difs.append(dif)
    difs.sort(reverse=True)
    return sum(difs[:k])


n, k = map(int, input().split())
nums = input().split()
print(main(n, k, nums))