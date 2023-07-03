# %%
from setuptools import find_packages
from setuptools import setup

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

find_packages()
# %%
setup(
    name='toolbox',
    version='1.0.0',
    author='terry97-guel',
    author_email='taerimyoon@korea.ac.kr',
    license='Apache License 2.0',
    description='Python toolbox for Robotics and Machine Learning',
    packages=find_packages(exclude=['.xml', '.stl', 'urdf', ]),
    # package_data={'toolbox': ['resources/assets/*.xml', 'resources/assets/*.urdf', 'resources/assets/*.stl']},
    # install_requires = read_requirements("requirements.txt"),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)