from setuptools import setup


def pre_install():
    f = open("readme.md", "r")
    text = f.read()
    return text

setup(
    name="face-identification",
    version="1.0.0", 
    author="Parisa Bagherzadeh", 
    description="A package to identify faces on an image",
    long_description=pre_install(),
    install_requires=['opencv-python', 'numpy', 'matplotlib', 'insightface'],
)