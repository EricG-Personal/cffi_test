from setuptools import setup, find_packages

requirements = [
    'cffi'
]

setup_requirements = [
    'cffi'
]

setup(
    name = 'cffi_test',
    packages = find_packages( include = [ 'cffi_test' ] ),
    install_requires = requirements,
    setup_requires = setup_requirements,
    cffi_modules = [ "c_library/build_sample_lib.py:ffibuilder" ]
)