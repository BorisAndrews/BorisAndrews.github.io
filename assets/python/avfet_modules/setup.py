from setuptools import setup, find_packages

setup(
    name='avfet_modules',
    version='0.3',
    description="Legacy modules for finite elements in time from Boris Andrews's thesis",
    long_description=open('README.txt').read(),
    author='Boris D. Andrews',
    packages=find_packages(),
    install_requires=[],
)
