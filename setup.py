import os
from setuptools import setup, find_packages
import numpy

# Read requirements from the existing pinned requirements file
requirements_path = os.path.join('etc', 'requirements', 'requirements.txt')
with open(requirements_path) as f:
    # Filter out comments and empty lines
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    # Remove any unsafe packages or version specifiers that setuptools can't handle
    requirements = [req for req in requirements if not req.startswith('# The following packages')]
setup(
    name="platipath",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Omid Shams Solari",
    author_email="solari@berkeley.edu",
    description="A package for analyzing somatic mutations correlated with platinum-based treatment outcomes",
    keywords="bioinformatics, genomics, somatic mutations, platinum treatment",
    python_requires=">=3.8",
    tests_require=["pytest"],
    include_package_data=True,
    include_dirs=[numpy.get_include()],
)

