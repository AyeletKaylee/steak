def all_primes(m):
    primes = list()
    
    marked_prime = [True] * m
    marked_prime[0], marked_prime[1] = False, False
    
    for candidate in range(2, m):
        if marked_prime[candidate]:
            primes.append(candidate)

            for i in range(candidate * 2, m, candidate):
                marked_prime[i] = False
    
    return primes

print(all_primes(8))