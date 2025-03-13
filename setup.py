from setuptools import setup

setup(
    name="skip-pip",
    version="0.1.2",
    py_modules=["pip_wrapper"],
    entry_points={
        "console_scripts": [
            "skip-pip=pip_wrapper:main",
        ],
    },
    author="Your Name",
    author_email="adupanithinsai@gmail.com",
    description="A pip wrapper that installs packages from requirements files while skipping packages that fail.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/saiadupa/skip-pip",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
