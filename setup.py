
"""Set up file for data-structures."""

from setuptools import setup

setup(
    name="data-structures",
    description="implementation of various data structures in python",
    author="Max Wolff, Chris Closser",
    author_email=["maxawolff@hotmail.com", "insert chris email here"],
    py_modules=["linked_list"],
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "pytest-watch", "tox"],
        "development": ["ipython"]
    },
    entry_points={
    }
)
