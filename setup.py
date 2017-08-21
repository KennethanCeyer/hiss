from setuptools import setup, find_packages
from codecs import open
from os import path, walk

name = 'hiss'
cwd = path.abspath(path.dirname(__file__))
packages = []
long_description = open(path.join(cwd, 'README.rst'), encoding='utf-8').read()

for dirname, dirnames, filenames in walk(name):
    if '__init__.py' in filenames:
        packages.append(dirname.replace('/', '.'))

setup(
    name='hiss-cli',
    version='0.0.1',
    description='Python database migration tool based on git\'s design.',
    long_description=long_description,
    url='https://github.com/KennethanCeyer/hiss',
    author='PIGNOSE',
    author_email='kennethan@nhpcw.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='hiss revision database cli version control',
    packages=packages + find_packages(exclude=[
        'contrib',
        'docs',
        'tests'
    ]),
    install_requires=['sqlalchemy'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest', 'coverage']
    }
)
