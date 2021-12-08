from setuptools import setup

setup(name='mercupy_parser',
      version='0.1.1',
      description='Python wrapper for mercury-parser',
      url='https://github.com/nikosNalmpantis/mercupy-parser',
      author='Nikos Nalmpantis',
      author_email='nikosnalmpantis@outlook.com',
      license='GNU General Public License v3.0',
      packages=['mercupy_parser'],
      install_requires=[
          'httpx',
          'validators',
      ],
      zip_safe=False)
