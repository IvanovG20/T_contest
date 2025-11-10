def main(a):
    mapp = {
        'price': a[0],
        'mb': a[1],
        'surcharge': a[2],
        'new_mb': a[3]
    }
    if mapp['new_mb'] > mapp['mb']:
        return mapp['price'] + (
            mapp['new_mb'] - mapp['mb']
        ) * mapp['surcharge']
    else:
        return mapp['price']


a = list(map(int, input().split()))
print(main(a))
