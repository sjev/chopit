# a_models docs

This is documentation for chopit

## How it works

* `mkdocs` documentation generator parses `.md` files in `docs` directory
* `mkdocstrings` extension parses `.py` libraries and generates documentation from code
* to keep it DRY, consider symlinking `README.md` to `docs` folder.


## Serving documentation locally

run `mkdocs serve` from `docs` folder

## Guiedlines for writing documentation

* write documentation as close as possible to the code. Module and function docstrings are the best place, followed by a README.md in the same folder etc.


## Refereneces

* [material theme](https://squidfunk.github.io/mkdocs-material/)
* [documenting with mkdocstrings](https://chrieke.medium.com/documenting-a-python-package-with-code-reference-via-mkdocs-material-b4a45197f95b)