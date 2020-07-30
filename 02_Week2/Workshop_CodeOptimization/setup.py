import numpy
from numpy.distutils.core import Extension
from numpy.distutils.core import setup


fortranExt = Extension(name="wave_propogation", sources=["wave_propogation.f90"])


setup(
    name="wave_propogation",
    description="Fortran library to compute wave propogation in a box",
    ext_modules=[fortranExt],
)
