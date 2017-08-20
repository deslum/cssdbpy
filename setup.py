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
                   Extension("cssdbpy.pool", ["cssdbpy/pool.pyx"]),
                   ]
    cmdclass = {'build_ext': build_ext}
else:
    cmdclass = {}
    ext_modules = [Extension("cssdbpy.cssdbpy", ["cssdbpy/cssdbpy.c"]),
                    Extension("cssdbpy.pool", ["cssdbpy/pool.c"]),
                   ]
setup(
    name='cssdbpy',
    version='0.1.1',
    packages=['cssdbpy'],
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    author='Yuri Bukatkin',
    author_email='randomazer@gmail.com',
    url='https://github.com/cssdbpy',
    description='High performance SSDB client implemented with Cython',
    data_files = [('', ['LICENSE'])]
)
