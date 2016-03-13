from pathlib import Path

from setuptools import setup, find_packages

exec(Path('version.py').read())

setup(
    name='tryp',
    description='tryp tools',
    version=version,  # NOQA
    author='Torsten Schmits',
    author_email='torstenschmits@gmail.com',
    license='MIT',
    url='https://github.com/tek/tryp',
    packages=find_packages(exclude=['unit', 'unit.*']),
    install_requires=[
        'fn',
        'toolz',
    ]
)
