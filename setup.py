from setuptools import setup, find_packages

setup(
    name="jinjatopdf",
    version='0.1',
    author="Vladimir Kipiani",
    author_email="inweb24.vk@gmail.com",
    packages=find_packages(),
    # install_requires=[
    #     'selenium>=3.0.2',
    #     'behave',
    #     'requests'
    # ],
    # package_data={
    #     'tc_selenium': [
    #         'features/*.feature',
    #         'drivers/chromedriver',
    #         'drivers/firefoxdriver',
    #         'drivers/darwin/chrome'
    #     ],
    # },
    entry_points={
        'console_scripts':
            ['jinjatopdf = jinjatopdf.app:main']
    },
)
