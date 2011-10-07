from setuptools import setup
from setuptools.extension import Extension

setup(
    name = "tps",
    version = "0.1",
    description='Thin plate spline transformation',
    author = "Oliver Tonnhofer",
    author_email = "olt@omniscale.de",
    license='MIT',
    packages=['tps', 'tps.test'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: C++",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
    ],
    test_suite = 'tps.test.test_suite',
    ext_modules=[
        Extension("tps._tps", ["tps/_tps.cpp", "tps/thinplatespline.cpp"], libraries=["stdc++"]),
    ],
)
