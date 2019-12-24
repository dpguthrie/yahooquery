from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="yahooquery",
    version="1.0.6",
    author="Doug Guthrie",
    author_email="douglas.p.guthrie@gmail.com",
    description="Retrieve nearly all data from Yahoo Finance for one or more ticker symbols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    url="https://github.com/dpguthrie/yahooquery",
    install_requires=['pandas>=0.24', 'requests>=2.20'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Operating System :: OS Independent"
    ],
    keywords='pandas, yahoo finance, finance, stocks, mutual funds, etfs'
)
