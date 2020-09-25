import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_package",
    version="0.0.1",
    author="Thomas Rommel",
    author_email="thomas@4thqa.io",
    description="Test package hosted on github",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4thQuarter-Analytics/4thqa-backend-test-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)