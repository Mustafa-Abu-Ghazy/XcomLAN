# -*- coding: utf-8 -*-
import os

import setuptools

current_directory = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="XcomLAN",
    version="0.0.1",
    author="Mustafa M. A. U. AbuGhazy",
    author_email="moustafa.abu.ghazy@gmail.com",
    maintainer_email="moustafa.abu.ghazy@gmail.com",
    description="Python library to access Studer-Innotec Xcom-LAN/Xcom-232i node "
                "through (SCOM) Xtender Serial Protocol "
                "over a TCP/IP Network connection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/XcomLAN/",
    project_urls={
        "Documentation": "https://mustafa-abu-ghazy.github.io/XcomLAN/",
        "Issues tracker": "https://github.com/mustafa-abu-ghazy/XcomLAN/issues",
        "Source Code": "https://github.com/mustafa-abu-ghazy/XcomLAN",
    },
    packages=setuptools.find_packages(),
    # packages=['XcomLAN', 'XcomLAN.device', 'XcomLAN.node_manager', 'XcomLAN.thingsboard'],
    include_package_data=True,
    license="MIT",
    platforms='any',
    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",

        "License :: OSI Approved :: MIT License",

        "Natural Language :: English",

        "Operating System :: OS Independent",

        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

        "Topic :: Communications",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",

        "Topic :: System :: Monitoring",

        "Topic :: Terminals :: Serial",
    ],
    python_requires=">=3.6",
    install_requires=["scom==0.7.3", "Cython", "pyserial>=3.5", "python-dotenv"],
    extras_require={
        'ThingsBoard': ['tb-mqtt-client'],
    },
)
