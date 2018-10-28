import os
from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        data = f.read()

    return data


setup(
    name='knapsack_problem',
    version='1.0',
    description="Knapsack problem solver",
    author='Dmitry Zhigailo',
    author_email='Dmitry.zhigailo@gmail.com',
    url="https://github.com/dzhigailo",
    scripts=["start_app.py"],
    packages=['knapsack_problem'],
    package_data={'knapsack_problem': ['data/*.csv']},
    long_description=read("README")
)
