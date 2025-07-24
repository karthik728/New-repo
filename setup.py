from setuptools import find_packages,setup

from typing import List

Hypen_dot = "-e ."
def get_requirements(file_path:str)-> List[str]:
    "This function will return the list of requirements"
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")for req in requirements]

        if Hypen_dot in requirements:
            requirements.remove(Hypen_dot)
    
    return requirements


# Meta data version of our project
setup(
name = "MlProject",
version = "0.0.1",
author = "Karthik",
author_email="kk5716117@gmail.com",
# This is very Powerful
packages = find_packages(),
requires = get_requirements("requirements.txt")
)