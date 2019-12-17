from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    with open(filename) as f:
        required = f.read().splitlines()
        return required


setup(
    name="yahooquery",
    version="0.0.1",
    author="Doug Guthrie",
    author_email="douglas.p.guthrie@gmail.com",
    description="Retrieve data from Yahoo finance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Operating System :: OS Independent"
    ],
    keywords='pandas, yahoo finance, finance'
)
