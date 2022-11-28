import setuptools

with open('../README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='emo-connect-python',
    version='0.0.1',
    author='Clark Scheff',
    author_email='clark@scheffsblend.com',
    description='Python library for connecting and interacting with an EMO pet',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/0xD34D/emo-connect-python',
    packages=setuptools.find_packages(
        include=['emoconnect*'],
        exclude=['examples*'],
    ),
    install_requires=[
        'bleak',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPLv3',
        'Operating System :: OS Independent',
    ],
)
