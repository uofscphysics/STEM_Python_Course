# ^ remove these two lines %%cython has to be the first line
%%cython -a
import time
# Import the c versions of pi and sin to speed up computations
from libc.math cimport M_PI as pi
from libc.math cimport sin as sin
cimport cython

cimport numpy as np
import numpy as np

# Using array to make C style array
from cython.view cimport array

# These turn off some python features for accessing arrays as python arrays
@cython.boundscheck(False)
@cython.wraparound(False)
# This turns off checks for divide by 0 and will seg fault instead of throw a warning
@cython.cdivision(True)
# Gave all the input variables types
def wave_propogation_fast(int num_steps, int scale,float damping,float initial_P,int stop_step):
    # Give types to variables we use to calculate with
    cdef float omega =  3.0 / (2.0 * pi)
    cdef int size_x = 2 * scale + 1
    cdef int size_y = 2 * scale + 1

    # Give types to loop iterator variables to make loops C loops
    cdef int i = 0
    cdef int j = 0
    cdef int step = 0

    # Setup
    cdef float [:,:] P = array(shape=(size_x, size_y), itemsize=sizeof(float), format="f")
    P[:,:] = 0.0
    cdef float [:,:,:] V = array(shape=(size_x, size_y, 4), itemsize=sizeof(float), format="f")
    V[:,:,:] = 0.0

    P[scale][scale] = initial_P

    for step in range(num_steps):
        if(step <= stop_step):
            P[scale][scale] = initial_P * sin(omega * step)
        for i in range(size_y):
            for j in range(size_x):
                V[i][j][0] = V[i][j][0] + P[i][j] - P[i - 1][j] if i > 0 else P[i][j]
                V[i][j][1] = V[i][j][1] + P[i][j] - P[i][j + 1] if j < size_x - 1 else P[i][j]
                V[i][j][2] = V[i][j][2] + P[i][j] - P[i + 1][j] if i < size_y - 1 else P[i][j]
                V[i][j][3] = V[i][j][3] + P[i][j] - P[i][j - 1] if j > 0 else P[i][j]

        for i in range(size_y):
            for j in range(size_x):
                P[i][j] -= 0.5 * damping * (V[i][j][0]+V[i][j][1]+V[i][j][2]+V[i][j][3])
    return np.asarray(P)
