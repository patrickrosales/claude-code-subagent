from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
    "pytest>=7.0.0",
    "flake8>=6.0.0",
    ],
)
