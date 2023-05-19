from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_des = str(f.read())

setup(
    name='swoopyui',
    version='1.1.1',
    author='SKbarbon',
    description='A python library that allow you to build swiftUI apps using python.',
    long_description=long_des,
    long_description_content_type='text/markdown',
    url='https://github.com/SKbarbon/swoopyui',
    install_requires=["flask"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)
