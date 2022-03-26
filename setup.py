# !/usr/bin/env python3

from setuptools import setup
from setuptools import find_namespace_packages

setup(
    
    name = "detection",

    author = "wishva peiris",

    author_email = "wishvaravindu666@gmail.com",

    #define the version of this library.
    #   -MAJOR VERSION 0
    #   -MINOR VERSION 1
    #   -MAINTAINCE VERSION 0
    version = "0.1.0",

    description = "This is a road anomaly detection application which is still int development",

    long_description = "the long description of the application",

    url = 'https://github.com/wishvaRavindu/Desktop-App-Final-Year-Project.git',

    install_requires = [
        "opencv-python>=4.2.0.32",
        "eel>=0.13.0",
        "pybase64>=1.1.0"
    ],

    keywords = "road anomalies, governments",
    
    packages = find_namespace_packages(
        where = ['project_files']
    ),
    package_data = {
        'project_files':['web/*']
    },

    include_package_data= True,

    python_requires='>=3.7',

    classifiers=[
         # I can say what phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Here I'll add the audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Transport industry',

        # Here I'll note that package was written in English.
        'Natural Language :: English',

        # Here I'll note that any operating system can use it.
        'Operating System :: OS Independent',

        # Here I'll specify the version of Python it uses.
        'Programming Language :: Python :: 3.8',

        # Here are the topics that my library covers.
        'Topic :: Database',
        'Topic :: Education',
        'Topic :: Office/Business'
    ]
)
