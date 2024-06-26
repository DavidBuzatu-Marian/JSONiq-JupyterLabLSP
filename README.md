# jsoniq-jupyter-lsp

[![PyPI version](https://badge.fury.io/py/jsoniq-jupyter-lsp.svg)](https://badge.fury.io/py/jsoniq-jupyter-lsp)
[![License](https://img.shields.io/badge/license-apache-blue.svg)](https://opensource.org/license/apache-2-0)

`jsoniq-jupyter-lsp` is a Python package that provides a language server setup for the JSONiq programming language. This package includes the necessary configuration to enable JSONiq to work seamlessly with the JupyterLab Language Server Protocol (LSP) extension, offering rich language features to users of JupyterLab.

## Features

- **Language Server for JSONiq**: Implements the Language Server Protocol (LSP) for JSONiq.
- **JupyterLab Integration**: Configures JupyterLab to recognize and use the JSONiq language server.
- **Rich Language Features**: Provides autocompletion, diagnostics, and other language features for JSONiq in JupyterLab.

## Installation

You can install the `jsoniq-jupyter-lsp` package using pip:

```bash
pip install jsoniq-jupyter-lsp
```

## Usage

To use the JSONiq language server in JupyterLab, follow these steps:

1. **Install JupyterLab and the JupyterLSP extension**:

   ```bash
   pip install 'jupyterlab>=4.1.0,<5.0.0a0' jupyterlab-lsp
   ```

2. **Install the `jsoniq-jupyter-lsp` package**:

   ```bash
   pip install jsoniq-jupyter-lsp
   ```

3. **Start JupyterLab**:

   ```bash
   jupyter lab
   ```

4. **Open a JSONiq file**: Open a `.jq` or `.ipynb` file in JupyterLab to start using the language server features.

## Configuration

By default, `jsoniq-jupyter-lsp` will be automatically configured to work with JupyterLab. However, you can customize the configuration if needed.

## Contributing

We welcome contributions to the `jsoniq-jupyter-lsp` project! If you have any suggestions, bug reports, or pull requests, please feel free to subapache them on the [GitHub repository](https://github.com/DavidBuzatu-Marian/JSONiq-JupyterLabLSP).

### Development Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DavidBuzatu-Marian/JSONiq-JupyterLabLSP.git
   cd jsoniq-jupyter-lsp
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the package in development mode**:

   ```bash
   pip install -e .
   ```

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.
