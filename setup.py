"""setup module"""
from setuptools import setup, find_packages

from pywnedpasswords import __version__

setup(name="pywnedpasswords",
      version=__version__,
      description="Client for HIBP passwords api using K-Anonymity method",
      url="http://github.com/xmatthias/pywnedpasswords",
      author="Matthias Voppichler",
      author_email="xmatthias@outlook.com",
      license="MIT License",
      scripts=["pywnedpasswords/pywnedpasswords.py"],
      python_requires='>=3',
      packages=find_packages(),
      install_requires=[
          "requests>=2"
      ],
      zip_safe=False,
      keywords=["pwnedpasswords", "passwords", "pwned", "security"]
      project_urls={
          "Source Code": "http://github.com/xmatthias/pywnedpasswords",
      }
      )
