from setuptools import setup, find_packages

setup(
    name="cowords",
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pdfminer',
        'Click'
    ],
    entry_points='''
        [console_scripts]
        cowords=toolMsl.main:init
    '''
)