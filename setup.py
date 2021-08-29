from setuptools import setup, find_packages

setup(
    name="labo",
    version="0.1.0",
    license="MIT",
    author="Douwe Hoekstra",
    packages=find_packages(),
    install_requires=["Click", "Jinja2", "tomli", "rich"],
    entry_points={
        "console_scripts": [
            "labo = labo.main:cli",
        ],
    },
)
