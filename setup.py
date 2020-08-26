from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='kaprekar_constant',  
    version='0.0.1',
    author="Shashank Deshpande",
    author_email="shashankdeshpande18@gmail.com",
    description="Kaprekar's Constant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shashankdeshpande/kaprekar-constant",
    packages=find_packages()
    )
