from setuptools import setup, find_packages

version_parts = (12, 5, 4)
version = '.'.join(map(str, version_parts))

setup(
    name='amino',
    description='functional data structures and type classes',
    version=version,
    author='Torsten Schmits',
    author_email='torstenschmits@gmail.com',
    license='MIT',
    url='https://github.com/tek/amino',
    packages=find_packages(exclude=['unit', 'unit.*']),
    install_requires=[
        'toolz',
        'lenses==0.1.7',
    ],
    tests_require=[
        'kallikrein',
    ],
)
