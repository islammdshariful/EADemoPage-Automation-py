# Selenium Python Test Automation (EA Demo Page)

This repository contains an automated testing framework for web applications using Selenium and Python 3.10. It includes sample test cases for demonstration for [Essential Addons for Elementor](https://essential-addons.com/elementor/demos/) demo page.

## Requirements

- Python 3.10
- virtualenv
- selenium 
- pytest

Please note that you do not have to install the any Chrome driver separately, as this repository uses Selenium v4.6.1, which automatically downloads and runs the driver during test execution.

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment using `virtualenv`:

```sh
$ virtualenv venv
```
3. Activate the virtual environment:
```sh
$ source venv/bin/activate
```
4. Install the required packages using pip:
```sh
$ pip install -r requirements.txt
```

## Usage
1. Activate the virtual environment:
```sg
$ source venv/bin/activate
```
2. Run the tests:
```sh
$ pytest test/test_all_widgets.py
```
3. Deactivate the virtual environment:
```sh
$ deactivate
```

## Contributions
Contributions to this repository are welcome. If you find any issues or have any suggestions for improvements, please submit a pull request or create an issue.
