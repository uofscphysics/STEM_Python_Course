# ^ remove these two lines %%cython has to be the first line
%%cython -a

cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def mat_mul_cy_fast(float[:,:] A, float[:,:] B, float[:,:] C):
    cdef int n = A.shape[0]
    cdef int i,j,k
    cdef float a
    for i in range(n):
        for k in range(n):
            a = A[i,k]
            for j in range(n):
                C[i,j] += (a * B[k,j])
