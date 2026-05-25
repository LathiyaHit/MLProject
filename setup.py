from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="MLProject",
    version="0.1.0",
    author="Hit",
    author_email="lathiyahit2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) ## Setup function is used to define the package and its dependencies. It takes several arguments such as name, version, author, author_email, packages, and install_requires. The install_requires argument is used to specify the dependencies of the package, which are read from the requirements.txt file using the get_requirements function.


