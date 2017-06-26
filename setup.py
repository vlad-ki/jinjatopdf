from setuptools import setup, find_packages

setup(
    name="jinjatopdf",
    version='0.1',
    author="Vladimir Kipiani",
    author_email="inweb24.vk@gmail.com",
    packages=find_packages(),

    entry_points={
        'console_scripts':
            ['jinjatopdf = jinjatopdf.app:main']
    },
)
