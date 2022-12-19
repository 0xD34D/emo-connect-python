from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='emo-connect-python',
    version='0.1.2',
    packages=find_packages(
        include=['emoconnect*'],
        exclude=['examples*', 'tests*'],
    ),
    author='Clark Scheff',
    author_email='clark@scheffsblend.com',
    description='Python library for connecting and interacting with an EMO pet',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/0xD34D/emo-connect-python',
    install_requires=[
        'bleak',
        'bleak-retry-connector',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
