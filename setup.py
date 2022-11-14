import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="KommatiParaClients",
    version="0.0.1",
    author="Jacek Cieciura",
    author_email="jacek.cieciura@capgemini.com",
    description="Client dataset creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ...",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
