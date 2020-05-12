"""setup module"""
from setuptools import setup, find_packages
import os

from pywnedpasswords import __version__

readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
with open(readme_file) as f:
    readme = f.read()

setup(
    name="pywnedpasswords",
    version=__version__,
    description="Client for HIBP passwords api using K-Anonymity method",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="http://github.com/xmatthias/pywnedpasswords",
    author="Matthias Voppichler",
    author_email="xmatthias@outlook.com",
    license="MIT",
    entry_points="""
      [console_scripts]
      pywnedpasswords=pywnedpasswords.pywnedpasswords:main
      """,
    python_requires=">=3",
    packages=find_packages(),
    install_requires=["requests>=2"],
    zip_safe=False,
    keywords=["pwnedpasswords", "passwords", "pwned", "security"],
    project_urls={"Source Code": "http://github.com/xmatthias/pywnedpasswords"},
)
