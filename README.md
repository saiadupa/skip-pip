# Skip-Pip

Skip-Pip is a command-line tool that acts like pip but with enhanced resilience during package installation. When installing from a requirements file, it skips packages that fail to install while continuing with the rest.

## Features

- **Resilient Installation:** Installs each package individually from requirements files.
- **Error Logging:** Prints error details for packages that fail to install.
- **Familiar Interface:** Supports standard pip commands and arguments.

## Installation

You can install Skip-Pip via pip (after publishing on PyPI):

```bash
pip install skip-pip
```

## Usage

Use `skip-pip` in place of `pip`. Here are a few examples:

- **Installing from a Requirements File:**

  ```bash
  skip-pip install -r requirements.txt
  ```

  This command reads the `requirements.txt` file, installs each package one by one, and prints a summary of any packages that failed to install.

- **Installing a Specific Package:**

  ```bash
  skip-pip install requests
  ```

  This installs the `requests` package.

- **Passing Additional Pip Arguments:**

  You can also pass extra pip arguments, such as upgrading packages:

  ```bash
  skip-pip install -r requirements.txt -- --upgrade
  ```

  The `--` separator indicates that the following options should be forwarded to pip.
