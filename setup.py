import os.path
from setuptools import setup, find_packages


def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()

setup(
    name="battleships",
    version="0.0.1",
    description="Battleships game",
    long_description=read_file("README.md"),
    author="Jo John and Jan",
    author_email="",
    license=read_file("LICENCE.md"),

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'battleships = battleships.cmd:main',
        ],
    },

    install_requires=[
                      "argcomplete",
                     ],
    tests_require=[
                    "pytest",
                    "flake8",
                  ],
)
