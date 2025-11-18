# setup.py

from setuptools import setup, find_packages


def readme():
    try:
        with open("README.rst", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


setup(
    name="pentatonics-matrix-cli",
    version="0.2.1",
    description="A modular CLI for exploring pentatonic substitutions across jazz harmony.",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    install_requires=[],  # No external dependencies now
    entry_points={
        "console_scripts": [
            "pentatonics=pentatonics_matrix_cli.cli:main",
        ]
    },
    license="MIT",
    url="http://github.com/yoshizzle/pentatonics-matrix-cli",
    author="Josh Sager",
    author_email="js1@joshsager.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education :: Music",
        "Intended Audience :: Musicians",
        "Environment :: Console",
    ],
    zip_safe=False,
)
