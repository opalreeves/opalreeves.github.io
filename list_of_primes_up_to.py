def list_of_primes_up_to(limit=100):
    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False
    for i in range(4, limit + 1, 2):
        primes[i] = False
    divisor = 3
    while divisor <= limit ** 0.5:
        if primes[divisor]:
            for multiple in range(divisor * 2, limit + 1, divisor):
                primes[multiple] = False
        divisor += 1
    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    return prime_numbers
