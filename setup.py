from distutils.core import setup
from distutils.extension import Extension

setup(
	name="sharp",
	version="1.0.1",
	author="Sigurd Naess",
	author_email="sigurdkn@astro.uio.no",
	description=("Wrapper for the libsharp spherical harmonics transofrm library"),
	long_description=("A python wrapper of the libsharp spherical harmonics "
		"transform library, from before libsharp got its own wrapper. This "
		"version used to be more general, but that may no longer be the case."),
	download_url = 'https://github.com/amaurea/sharp/tarball/1.0.1',
	license = "CC0",
	keywords = "science spherical harmonics transform",
	url = "http://packages.python.org/sharp",
	classifiers=[
		"Topic :: Scientific/Engineering",
		"License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
	],
	ext_modules = [
		Extension(
			name="sharp",
			sources=["sharp.c"],
			libraries=["sharp","c_utils","fftpack"],
			include_dir=["."],
			extra_link_args = ["-fopenmp"],
		)
	]
)
