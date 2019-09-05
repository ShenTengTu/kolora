from setuptools import setup, find_packages
from os import path
from kolora import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kolora",
    version=__version__,
    description="Use method chain to make colored text in terminal.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ShenTengTu/kolora",
    author="Shen-Teng Tu",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Terminals",
    ],
    keywords=["color", "koloro", "kolora", "ansi", "terminal", "linux", "python"],
    packages=find_packages(exclude=["test"]),
    python_requires=">=3.6",
)
