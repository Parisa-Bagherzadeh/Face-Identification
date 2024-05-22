from setuptools import setup


def pre_install():
    f = open("readme.md", "r")
    text = f.read()
    return text

setup(
    name="sajjad",
    version="1.0.0", 
    author="Sajjad", 
    description="prints a cow",
    long_description=pre_install(),
    requires=[]
)