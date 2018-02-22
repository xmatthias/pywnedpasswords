"""setup module"""
from setuptools import setup, find_packages
import os

from pywnedpasswords import __version__

readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
try:
    from m2r import parse_from_file
    readme = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    print("for releases, please install m2r!")
    with open(readme_file) as f:
        readme = f.read()

setup(name="pywnedpasswords",
      version=__version__,
      description="Client for HIBP passwords api using K-Anonymity method",
      long_description=readme,
      url="http://github.com/xmatthias/pywnedpasswords",
      author="Matthias Voppichler",
      author_email="xmatthias@outlook.com",
      license="MIT",
      scripts=["pywnedpasswords/pywnedpasswords.py"],
      python_requires='>=3',
      packages=find_packages(),
      install_requires=[
          "requests>=2"
      ],
      zip_safe=False,
      keywords=["pwnedpasswords", "passwords", "pwned", "security"],
      project_urls={
          "Source Code": "http://github.com/xmatthias/pywnedpasswords",
      }
      )
