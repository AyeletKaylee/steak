def simple_gcd(x, y):
    # starts at the smaller number and goes down to 1 since there is no point in
    # checking numbers bigger than the smaller number - if the smaller number is
    # not a common divisor, the bigger number can't be either
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
        