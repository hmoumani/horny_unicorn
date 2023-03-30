from setuptools import setup
from setuptools import find_packages

print(find_packages(where="src/"))

setup(
    name='my_minipack',
    version='1.0.0',
    author='hmoumani',
    url='None',
    description='Howto create a package in python.',
    install_requires=[],
    author_email="hmoumani@studnet.1337.ma",
    packages=find_packages(where="src/"),
    package_dir={"": "src/"},
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education"
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ],
)
