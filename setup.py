from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Function will return the list of requirements from a given file.'''

    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='machine learning project',
    version='1.0.0',
    author='Swaroop',
    author_email='swaroopudgaonkar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    )