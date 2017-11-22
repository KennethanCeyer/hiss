import os
from utils.util_file import read, find_version

from setuptools import setup, find_packages

name = 'hiss'
version = find_version(name, '__init__.py')
cwd = os.path.abspath(os.path.dirname(__file__))
long_description = read(os.path.join(cwd, 'README.rst'), encoding='utf-8')

setup(
    name='hiss-cli',
    version=version,
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
    packages=find_packages(exclude=[
        'contrib',
        'build',
        'docs',
        'tests'
    ]),
    install_requires=[
        'six',
        'SQLAlchemy'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coveralls', 'pytest', 'coverage']
    },
    entry_points={
        'console_scripts': [
            'hiss=hiss.hiss_cli:main'
        ]
    }
)
