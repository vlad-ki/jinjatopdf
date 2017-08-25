from setuptools import setup, find_packages

setup(
    name="jinjatopdf",
    version='0.9',
    author="Vladimir Kipiani",
    author_email="inweb24.vk@gmail.com",
    classifiers=[
                 "Operating System :: POSIX",
                 "Programming Language :: Unix Shell",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    install_requires=[
        'jinja2',
        'zope.dottedname',
        'yaml',
    ],

    entry_points={
        'console_scripts':
            ['jinjatopdf = jinjatopdf.__main__:main']
    },
)
