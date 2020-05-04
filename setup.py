import setuptools
from pathlib import Path


SCRIPTS = [str(f) for f in Path('scripts').glob('*program.py')]
long_description = "some text"

setuptools.setup(
    name="get_volumes",
    version="0.0.1",
    author="Damien Ferhadian",
    author_email="dferhadian@egmail.com",
    description="A package that will calculate the volume of DNA needed to get 700 micro-gram of DNA after Nanodrop measurement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dferhadian/-project_spring_2020/tree/master/get_volumes",
    packages=setuptools.find_packages(),
    scripts = SCRIPTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
