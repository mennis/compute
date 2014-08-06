from setuptools import setup, find_packages

setup(
    name="compute",
    url='https://github.com/mennis/compute',
    description="Some pure python Math and Physics tools. ",
    author='michaelian ennis',
    packages=find_packages('compute'),
    package_dir={'': 'compute'},
    test_suite='nose.collector',
    tests_require=['nose', 'numpy'],
    zip_safe=True
)
