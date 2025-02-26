from setuptools import setup, find_packages

setup(
    name="django_setup",
    version="0.1",
    packages=find_packages(),
    install_requires=["django", "django-environ"],
    entry_points={
        "console_scripts": [
            "djs=django_setup.cli:main",
        ],
    },
    author="DakDot",
    description="A Django project setup automation tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eliHeist/django_setup.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
