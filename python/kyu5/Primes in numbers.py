def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    # Construct the string representation of the prime factors
    result = ""
    for p in sorted(set(factors)):
        n = factors.count(p)
        result += "({}**{})".format(p, n) if n > 1 else "({})".format(p)
    return result