# ^ remove these two lines %%cython has to be the first line
%%cython -a
cimport cython

@cython.cdivision(True)
cdef inline double recip_square_cy(Py_ssize_t i):
    cdef:
        double x, s
    x = i*i
    s = 1 / x
    return s


def approx_pi_cy(int n):
    """Compute an approximate value of pi."""
    cdef:
        int k
        double val
    val = 0
    for k in range(1, n+1):
        x = recip_square_cy(k)
        val += x
    pi = (6 * val)**.5
    return pi
