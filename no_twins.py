def no_twins(n: int, x: int, y: int):
    if n == 0:
        return [[]]
    if n == 1:
        return [[x], [y]]

    else:
        l1, l2 = no_twins(n-1, x, y), no_twins(n-2, x, y)
        print('l2: ', l2)

        created_lists = [[x]+d for d in l1 ]+ [[y, x] + q for q in l2]
        
        to_return = created_lists
        return to_return

print(sorted(no_twins(2, 5, 3)))