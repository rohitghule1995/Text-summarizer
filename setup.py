import setuptools

with open("README.md","r", encoding="UTF-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-summarizer"
AUTHOR_USER_NAME = "Rohit Ghule"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rohitghule1995@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Python package for text summarization",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir = {"":"src"},
    package = setuptools.find_packages(where="src")
)