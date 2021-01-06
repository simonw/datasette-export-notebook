# datasette-export-notebook

[![PyPI](https://img.shields.io/pypi/v/datasette-export-notebook.svg)](https://pypi.org/project/datasette-export-notebook/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-export-notebook?include_prereleases&label=changelog)](https://github.com/simonw/datasette-export-notebook/releases)
[![Tests](https://github.com/simonw/datasette-export-notebook/workflows/Test/badge.svg)](https://github.com/simonw/datasette-export-notebook/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-export-notebook/blob/main/LICENSE)

UNDER CONSTRUCTION: Datasette plugin providing instructions for exporting data to Jupyter or Observable

## Installation

Install this plugin in the same environment as Datasette.

    $ datasette install datasette-export-notebook

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-export-notebook
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest
