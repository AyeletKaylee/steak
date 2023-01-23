def fast_pow(x: float, n: int):
    if n == 0:
        return 1

    power, remainder = divmod(n, 2)

    result = fast_pow(x, power)

    result *= result

    return result if not remainder else result * x


print(fast_pow(1, 100))


# example given by course: (approx)
def power(x, n):

    if n == 0:
        return 1

    y = power(x, n // 2)

    if n % 2 == 0:
        return y * y
    return y * y * x


# runtime complexity:
#   .oooooo.     .o oooo                                   o.
#  d8P'  `Y8b   .8' `888                                   `8.
# 888      888 .8'   888   .ooooo.   .oooooooo ooo. .oo.    `8.
# 888      888 88    888  d88' `88b 888' `88b  `888P"Y88b    88
# 888      888 88    888  888   888 888   888   888   888    88
# `88b    d88' `8.   888  888   888 `88bod8P'   888   888   .8'
#  `Y8bood8P'   `8. o888o `Y8bod8P' `8oooooo.  o888o o888o .8'
#                `"                 d"     YD              "'
#                                   "Y88888P'
