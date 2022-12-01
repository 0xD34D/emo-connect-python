from setuptools import find_packages, setup

with open('../README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='emo-connect-python',
    version='0.1.0',
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
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPLv3',
        'Operating System :: OS Independent',
    ],
)
