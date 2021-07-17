# simple example of setup file
# this file is needed to build local folder as pip package
# pip install .
from setuptools import setup

setup(name='veteraniusutil',
      version='0.1',
      description='Example utility package',
      author='Veteranius',
      license='MIT',
      packages=['util'],
      install_requires=['flake8'],
      zip_safe=False)
