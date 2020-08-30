from setuptools import find_packages, setup

setup(
    name="number_baseball_helper",
    version="0.0.1",
    description="Number Baseball Helper",
    author="NDK",
    author_email="klize31@gmail.com",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': [
            'nbhelper = number_baseball_helper.cmd.nbhelper:main',
            'nbnpc = number_baseball_helper.cmd.nbnpc:main'
        ],
    },
)
