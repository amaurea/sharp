from distutils.core import setup
from distutils.extension import Extension

setup(
	name="sharp",
	version="1.0.0",
	author="Sigurd Naess",
	author_email="sigurdkn@astro.uio.no",
	description=("A python wrapper of the libsharp spherical harmonics "
		"transform library, from before libsharp got its own wrapper. This "
		"version used to be more general, but that may no longer be the case."),
	license = "CC0",
	keywords = "science spherical harmonics transform",
	url = "http://packages.python.org/sharp",
	classifiers=[
		"Topic :: Scientific/Engineering",
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
