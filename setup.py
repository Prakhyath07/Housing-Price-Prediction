from setuptools import setup,find_packages
from typing import List


## variable declaration for setup
PROJECT_NAME="housing_price_predictor"
VERSION ="0.0.1"
AUTHOR="Prakhyath Bhandary"
DESCRIPTION="This project is to predict the house prices"
# PACKAGES=["housing"] ## instead we can use find_packages()
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is used to return  list
    of libraries required from requirements.txt

    return: List of libraries required


    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

