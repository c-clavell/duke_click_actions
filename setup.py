from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
name="demo-click",
version="0.0.1",
description="Click demo",
install_requires = ["click", "colorama"],
entry_points="""
[console_scripts]
clickDemo=clickFiles.click1:hello1
""",

author="Me",
author_email="me@me.com",
packages=find_packages(),

)