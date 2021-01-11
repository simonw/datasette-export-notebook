from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-export-notebook",
    description="Datasette plugin providing instructions for exporting data to Jupyter or Observable",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-export-notebook",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-export-notebook/issues",
        "CI": "https://github.com/simonw/datasette-export-notebook/actions",
        "Changelog": "https://github.com/simonw/datasette-export-notebook/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_export_notebook"],
    entry_points={"datasette": ["export_notebook = datasette_export_notebook"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "sqlite-utils"]},
    tests_require=["datasette-export-notebook[test]"],
    package_data={"datasette_export_notebook": ["templates/*.html"]},
    python_requires=">=3.6",
)
