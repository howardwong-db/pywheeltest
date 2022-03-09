from setuptools import setup
from setuptools import find_packages

VERSION = '0.0.1'
DESCRIPTION = 'pywheel test package.'
LONG_DESCRIPTION = 'some long pywheel test package'

# Setting up
setup(
    name='example_pkg',
    version=VERSION,
    author='Howard Wong',
    author_email='<xxxxxxxx@yyyyy.com>',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['main=example_pkg.main:main']
    }
)

