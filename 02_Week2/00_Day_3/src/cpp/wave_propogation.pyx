from libc.stdlib cimport malloc, free
from cpython.mem cimport PyMem_Malloc
import numpy as np
import time
cimport cython
from cython.view cimport array as cvarray

cdef extern from "wp.hpp":
  void wave_propogation_single_core(int, int, float, float, int, float*)

@cython.boundscheck(False)
@cython.cdivision(True)
@cython.wraparound(False)
@cython.infer_types(False)
def wave_propogation(int num_steps, int scale, float damping, float initial_P, int stop_step):
  cdef int size_x = 2 * scale + 1
  cdef int size_y = 2 * scale + 1
  cdef int i = 0
  cdef int j = 0
  cdef float *array = <float *> malloc(sizeof(float) * size_x * size_y)
  wave_propogation_single_core(num_steps, scale, damping, initial_P, stop_step, array)
  P = [[0.0 for x in range(size_x)] for y in range(size_y)]

  for i in range(size_x):
    for j in range(size_y):
      P[i][j] = array[i*size_x+j] if not np.isnan(array[i*size_x+j]) else 0.0
  return P
