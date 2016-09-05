#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
    have_cython = True
except ImportError:
    have_cython = False

if have_cython:
    ext_modules = [Extension("cssdbpy.cssdbpy", ["cssdbpy/cssdbpy.pyx"]),
                   ]
    cmdclass = {'build_ext': build_ext}
else:
    cmdclass = {}
    ext_modules = [Extension("cssdbpy.cssdbpy", ["cssdbpy/cssdbpy.c"]),
                   ]
setup(
    name='cssdbpy',
    version='0.0.1',
    packages=['cssdbpy'],
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    author='deslum',
    author_email='randomazer@gmail.com',
    url='https://github.com/cssdbpy',
    description='High performance SSDB client implemented with Cython',
    long_description=open('README.rst').read(),
)
