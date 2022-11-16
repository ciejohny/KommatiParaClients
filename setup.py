import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()
setuptools.setup(
    name="KommatiParaClients",
    version="1.0.1",
    author="Jacek Cieciura",
    author_email="jacek.cieciura@capgemini.com",
    description="Client dataset creation",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: ...",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    python_requires='>=3.7'
)
