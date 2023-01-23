import math

def is_prime(n: int):
    devisor = 2
    
    while devisor <= math.sqrt(n):
        if n % devisor == 0:
            return False
        devisor += 1
    
    return True


def is_prime_2(n: int):
    
    for devisor in range(2, math.sqrt(n) + 1):
        if n % devisor == 0:
            return False
    
    return True

