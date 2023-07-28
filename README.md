# Cookie's Utilities

Utility functions.

- [TestPyPI](https://test.pypi.org/project/cookies-utilities/)
- [Documentation](https://cookies-utilities.readthedocs.io/en/latest/index.html)

---

### Development Guide

Please execute the following at the root of the repository.

#### Test locally

Please run the following commands.

```
pip uninstall cookies_utilities  # uninstall the package if already installed
pip install -e .  #  install the package in editable mode
python -m unittest discover tests -v  # test
```
If an error occurs, you can fix the code and rerun the tests without having to reinstall the package.

#### Build the distribution archives

Please run the following commands. More details are [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives).

```
pip install --upgrade build  # upgrade 'build'
python -m build
```

The following files will be generated.

```
./dist/cookies_utilities-0.0.1.tar.gz
./dist/cookies_utilities-0.0.1-py3-none-any.whl
```

#### Upload the distribution archives to TestPyPI

Please run the following commands. More details are [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives).

```
pip install --upgrade twine
python -m twine upload --repository testpypi dist/*
```

