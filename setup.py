import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tkinterHelper",
    version="0.1.0",
    author="LupusCoding",
    author_email="dittrich.ralph@lupuscoding.de",
    description="A simple helper package to easily create tkinter objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lupuscoding/tkinterHelper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)