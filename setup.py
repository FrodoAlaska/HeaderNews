from setuptools import setup, find_packages

# Copy the contents of the README file as the description

with open("README.md", "r") as file: 
    desc = file.read()

# Setup the package

setup(
    name="HeaderNews", 
    version="0.1", 
    package=find_packages(),
    install_required=[
        "newsapi-python",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "headernews = HeaderNews:main",
        ],
    },
    long_description=desc, 
    long_description_content_type="text/markdown", 
)
