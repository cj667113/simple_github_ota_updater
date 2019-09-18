import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sgota",
    version="0.0.1",
    author="Christopher M Johnston",
    author_email="chris.johnston60.cj@gmail.com",
    description="OTA Github Updater",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cj667113/simple_github_ota_updater",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)

