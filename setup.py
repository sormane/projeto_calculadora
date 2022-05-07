from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ppackage_calc",
    version="0.0.1",
    author="sormane",
    author_email="sormaneguimaraes@gmail.com",
    description="Realização de cálculos básicos",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sormane/projeto_calculadora",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)
