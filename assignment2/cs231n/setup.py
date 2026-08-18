from Cython.Build import cythonize
import numpy
from setuptools import Extension, setup

extensions = [
    Extension(
        "im2col_cython",
        ["im2col_cython.pyx"],
        include_dirs=[numpy.get_include()],
    ),
]

setup(
    ext_modules=cythonize(extensions),
)