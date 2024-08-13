# %%
from setuptools import find_packages
from setuptools import setup

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

find_packages()
# %%
setup(
    name='terry_toolbox',
    version='1.0.1',
    author='terry97-guel',
    author_email='taerimyoon@korea.ac.kr',
    license='Apache License 2.0',
    description='Python toolbox for Robotics and Machine Learning',
    packages=find_packages(),
    package_data={'terry_toolbox': ['resources/assets/**']},
    install_requires = read_requirements("requirements.txt"),
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
)