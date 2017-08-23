from setuptools import setup, find_packages
import io
import os
import re


def read(*names, **kwargs):
    """Python 2 and Python 3 compatible text file reading.
    Required for single-sourcing the version string.
    """
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    """
    Search the file for a version string.
    file_path contain string path components.
    Reads the supplied Python module as text without importing it.
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


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
        'docs',
        'tests'
    ]),
    install_requires=['SQLAlchemy'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest', 'coverage']
    },
    entry_points={
        'console_scripts': [
            'hiss=hiss:hiss'
        ]
    }
)
