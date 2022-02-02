from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'A Terminal based digital diary'

# Setting up
setup(
    name="Moment Book",
    version=VERSION,
    author="PsyQuake (Vishesh Sharma)",
    author_email="<sharmavishesh022@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['mysql.connector','datetime','tabulate'],
    keywords=['python', 'book', 'diary', 'notepad', 'cli', 'mysql'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)