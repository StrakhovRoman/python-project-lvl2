# Difference generator #
## CLI utility compares two configuration files and shows a difference
***
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/StrakhovRoman/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6671e98d9a73da319483/test_coverage)](https://codeclimate.com/github/StrakhovRoman/python-project-lvl2/test_coverage)
[![Actions Status](https://github.com/StrakhovRoman/python-project-lvl2/workflows/PythonCI/badge.svg)](https://github.com/StrakhovRoman/python-project-lvl2/actions)
[![Actions Status](https://github.com/StrakhovRoman/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/StrakhovRoman/python-project-lvl2/actions)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)  
***
Use this command to install the package via Git:
```
python -m pip install git+https://github.com/StrakhovRoman/python-project-lvl2.git@0262c52cdfdaf2f8408551c5d5580bd587a47ae7
```
***
For help:
```
gendiff -h
```
```
usage: gendiff [-h] [-f FORMAT] first_file second_file
```
Supported compare file formats: .json, .yml

Supported output formats: plain, json and stylish format by default

***

### Default stylish format
[![asciicast](https://asciinema.org/a/Kxt0Bsa5iFVCbgWCR89dpWLXR.svg)](https://asciinema.org/a/Kxt0Bsa5iFVCbgWCR89dpWLXR)

### Plain format
[![asciicast](https://asciinema.org/a/LWgpMSt7dKRVmTNd9nvbMbH4S.svg)](https://asciinema.org/a/LWgpMSt7dKRVmTNd9nvbMbH4S)

### JSON format
[![asciicast](https://asciinema.org/a/pPR16DZWCVTLZLs0spYpzjYhm.svg)](https://asciinema.org/a/pPR16DZWCVTLZLs0spYpzjYhm)