def is_prime(possiblePrime):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
    return isPrime


def getPrimes_mp(max_num):
    primes = []
    # Use mp to make a list of true and false values
    with mp.Pool() as pool:
        __prime = pool.map(is_prime, range(max_num))

    # Loop over the numbers to make the list of numbers from the true/false list
    for possiblePrime in range(max_num):
        if __prime[possiblePrime]:
            primes.append(possiblePrime)

    return primes
