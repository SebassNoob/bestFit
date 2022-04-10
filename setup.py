from setuptools import setup, find_packages
setup(
  name = "bestFit",
  version='0.1',
  licence ="MIT",
  author = "SebassNoob",
  author_email="sebass#9507",
  packages=find_packages('src'),
  install_requires=[
    'numpy',
    'matplotlib'
  ],
  
  
)