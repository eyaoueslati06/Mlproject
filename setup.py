from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
## La ligne -e . dans requirements.txt est utilisée pour installer le projet actuel en mode éditable. Cependant, 
##cette ligne n'est pas une exigence de package standard et ne doit pas être passée à l'argument install_requires dans la fonction setup.

def get_requirements(file_path: str) -> List[str]:
    """ This function will return the list of requirements """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

## Directive du Mode Éditable : La directive -e . est spécifique à pip pour le développement local et ne doit pas être incluse dans la liste des packages que setuptools essaie d'installer.
setup(
    name='mlproject',
    version='0.0.1',
    author='Eya',
    author_email='eyaoueslati.oue@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
