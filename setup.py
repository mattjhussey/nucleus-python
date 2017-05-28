"""Setup file for install and test."""

import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    """Open a local file and return as string.

    Used for populating descriptions and arguments from file.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    """Run the setup."""
    setup(
        name="pybaseline",
        version="0.0.1",
        author="Matthew Hussey",
        author_email="matthew.hussey@googlemail.com",
        description=("Baseline python setup."),
        license="None, private use by myself only",
        keywords="python",
        url="none.non",
        entry_points={
            'console_scripts': [
                'pybaseline = pybaseline.__main__:main'
            ],
            'gui_scripts': [
                'pybaseline_ui = pybaseline.__main__:main_ui'
            ]},
        packages=find_packages(where='src'),
        package_data={
            'pybaseline': [
                'logging.conf'
            ]},
        package_dir={'': 'src'},
        install_requires=[],
        long_description=read("README"),
        classifiers=[
            "Development Status :: 1 - Planning"],
        setup_requires=[],
        tests_require=[]
    )

if __name__ == "__main__":
    main()
