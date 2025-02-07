from setuptools import find_packages,setup
from typing import List
def get_requires(file_path:str)-> List[str] :
    """This function read the required libraries that used in the project"""
    requirments = []
    with open(file_path) as file:
        requirments = file.readline()
        requirments = [req.replace("\n","") for req in requirments]
        if '-e .' in requirments :
            requirments.remove('-e .')
        return requirments

setup(
    name ="endtoendml",
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requires('requirments.txt')
)