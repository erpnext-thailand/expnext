from setuptools import setup, find_packages
import os

with open("requirements.txt", "r") as f:
    install_requires = f.read().strip().split("\n")

# Get version from __init__.py
from re import findall
with open(os.path.join("expnext", "__init__.py"), "r") as f:
    version = findall(r'__version__ = "(.*?)"', f.read())[0]

setup(
    name="expnext_accounting",
    version=version,
    description="ExpNext Accounting",
    author="limweb@hotmail.com",
    author_email="limweb@hotmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Framework :: Frappe",
    ],
)

