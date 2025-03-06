# Project Template

This is a Template Empty code base for quickly setup a structured, easy-to-manage code base for Machin Learning projects in 2025.

Supporting Features:

+ Conda enviroment managements (with some porpular ML package listed in `environment.yml`)
+ PEP 8 compliant package setup
+ Git Managements

## TODOs

+ [ ] Edit environment.yml file and Change `<package-name>`, edit dependencies.
+ [ ] Edit pyproject.toml file, Change `<package-name>` and `<Authors>`
+ [ ] Change the folder `package-name` at the project root to match the `<package-name>`



## Setup:

1. Conda env configuration:

```shell
conda env create -f environment.yml
```

+ if you wish to update environment dependencies (not recommended) please do:

```
conda env update --name <package-name> --file environment.yml --prune
```

+ if you wish to register this kernel to jupyterlab:

```shell
python -m ipykernel install --user --name="<package-name>" --display-name "<package-name>"
```


Package setup

```
pip install -e <path-to-folder-root>
```
