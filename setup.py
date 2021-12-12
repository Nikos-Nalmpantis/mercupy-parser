import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as f:
    long_description = f.read()


setup(
    name='mercupy_parser',
    version='0.2.1',
    description='Python wrapper for mercury-parser',
    long_description=long_description,
    url='https://github.com/nikosNalmpantis/mercupy-parser',
    author='Nikos Nalmpantis',
    author_email='nikosnalmpantis@outlook.com',
    license='GNU General Public License v3.0',
    packages=['mercupy_parser'],
    install_requires=[
      'httpx',
    ],
    zip_safe=False
)
