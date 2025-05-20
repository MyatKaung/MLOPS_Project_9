from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Project9",
    version="0.1",
    author="MyatKaung",
    packages=find_packages(),
    install_requires = requirements,
)