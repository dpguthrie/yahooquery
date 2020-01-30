from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'pandas',
    'requests-futures',
]

TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="yahooquery",
    version="1.1.3",
    author="Doug Guthrie",
    author_email="douglas.p.guthrie@gmail.com",
    description="Retrieve nearly all data from Yahoo Finance for one or more ticker symbols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    url="https://github.com/dpguthrie/yahooquery",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Intended Audience :: Financial and Insurance Industry",
        "Operating System :: OS Independent"
    ],
    keywords='pandas, yahoo finance, finance, stocks, mutual funds, etfs'
)
