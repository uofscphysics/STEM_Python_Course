# ^ remove these two lines %%cython has to be the first line
%%cython -a

cimport cython

cdef extern from "complex.h":
    double cabs(double complex)

# color function for point at (x, y)
cdef unsigned int mandel_cython(float x, float y, unsigned int max_iters):
    cdef double complex c, z
    c = x + y*1j
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if cabs(z) >= 2:
            return i
    return max_iters

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def create_fractal_cython(float xmin, float xmax, float ymin, float ymax, unsigned int[:, :] image, int iters):

    cdef int x, y
    cdef int height, width
    cdef double pixel_size_x, pixel_size_y
    cdef double real, imag
    cdef unsigned int color

    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (xmax - xmin)/width
    pixel_size_y = (ymax - ymin)/height

    for x in range(width):
        real = xmin + x*pixel_size_x
        for y in range(height):
            imag = ymin + y*pixel_size_y
            color = mandel_cython(real, imag, iters)
            image[y, x]  = color
