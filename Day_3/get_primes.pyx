# ^ remove these two lines %%cython has to be the first line
%%cython -a

cimport cython

@cython.cdivision(True)
def getPrimes_cy(Py_ssize_t max_num):
    primes = [2]
    cdef int possiblePrime = 0
    cdef int num = 0
    # Hint: Do we need to loop over every number??
    # What do we know about primes that could help us
    for possiblePrime in range(3, max_num, 2):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(3, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)

    return primes
