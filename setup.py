from setuptools import setup
import codecs


with codecs.open('README.rst', 'r', 'utf-8') as readme:
    long_description = readme.read()


setup(
    name='urlreplacer',
    packages=['urlreplacer'],
    version='0.1',
    description='Find and replace URLs in plain text messages',
    long_description=long_description,
    license='MIT',
    author='Tictail',
    author_email='tech+pip-urlreplacer@tictail.com',
    url='https://github.com/tictail/urlreplacer',
    keywords=['url', 'email', 'replace'],
    install_requires=['regex==2015.11.9'],
    extras_require={
        'tests': [
            'coverage==4.0.2',
            'pytest==2.8.2',
            'flake8==2.5.0'
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ],
)
