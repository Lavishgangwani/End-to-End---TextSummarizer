#setup.py

import setuptools

with open("README.md", mode="r", encoding="utf-8") as file:
    long_description = file.read()



__version__ = "0.0.0"

REPO_NAME = "End-to-End---TextSummarizer"
AUTHOR_USER_NAME= "LavishGangwani"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "lavishgangwani22@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A NLP Solution End-to-End Text Summarizer using Transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)