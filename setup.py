import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

os.umask(0o022)

setuptools.setup(
    name="ubuntu-security",
    version="0.1.0",
    author="Mike Salvatore <mike.salvatore@canonical.com>",
    description="Libraries used by the Ubuntu Security Team to facilitate vulnerability tracking and reporting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/canonical/ubuntu-security-lib",
    packages=setuptools.find_packages(exclude=["tests"]),
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
    ],
    install_requires=["ust-download-cache"],
    python_requires=">=3.5",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)
