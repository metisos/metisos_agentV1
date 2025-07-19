from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="metis-starter",
    version="0.1.0",
    author="Metis Agent Team",
    author_email="metis.agent.team@example.com",
    description="Starter kit for building agents with Metis Agent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/metis-team/metis-starter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "metis-agent>=0.1.0",
        "flask>=2.0.0",
        "python-dotenv>=0.15.0",
        "requests>=2.25.0",
    ],
)