from setuptools import setup, find_packages

setup(
    name="jinjatopdf",
    version='0.9',
    author="Vladimir Kipiani",
    author_email="inweb24.vk@gmail.com",
    packages=find_packages(),
    install_requires=[
        'jinja2',
        'zope.dottedname',
    ],

    entry_points={
        'console_scripts':
            ['jinjatopdf = jinjatopdf.__main__:main']
    },
)
