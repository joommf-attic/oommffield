from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='oommffield',
    version='0.1',
    description='A Python package for analysing and manipulating OOMMF vector field files',
    long_description=readme,
    author='Computational Modelling Group',
    author_email='fangohr@soton.ac.uk',
    packages=['oommffield', 'oommffield.tests'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
