#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from numpy.distutils.core import Extension
from os.path import join as pjoin

LIBNUFFT_VERSION = '1.3.2'
LIBNUFFT_SRCDIR = 'extern/libnufft-{}'.format(LIBNUFFT_VERSION)
LIBNUFFT_SRCFILES = [pjoin(LIBNUFFT_SRCDIR, srcfile) for srcfile in
        ('nufft1df90.f', 'nufft2df90.f', 'nufft3df90.f', 'dirft1d.f',
        'dirft2d.f', 'dirft3d.f', 'next235.f', 'dfft.f', 'dfftpack.f')]

ext = Extension(name = "nufft",
                sources = ['nufft.pyf',] + LIBNUFFT_SRCFILES,
                )

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(name = "python-nufft",
          description = "Python wrappers for Greengard and Lee's NUFFT",
          author = 'Ghislain Vaillant',
          author_email = 'ghislain.vaillant@kcl.ac.uk',
          license='BSD',
          ext_modules = [ext,],
          )
