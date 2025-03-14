from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements, dependency_links = [], []
    for line in f:
        (dependency_links if line.startswith("git+") else requirements).append(line.strip())

setup(
    name="window_manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    dependency_links=dependency_links,
    author="Sameer Arif",
    author_email="supersameer64@gmail.com",
    description="A class provides a convenient way to interact with application windows on your system. It allows you to find, select, and perform actions such as minimizing, maximizing, restoring, and closing windows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SameerArif64/Window-Manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)
