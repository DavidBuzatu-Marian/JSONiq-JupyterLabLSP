# jsoniq-jupyter-lsp

[![PyPI version](https://badge.fury.io/py/jsoniq-jupyter-lsp.svg)](https://badge.fury.io/py/jsoniq-jupyter-lsp)
[![License](https://img.shields.io/badge/license-apache-blue.svg)](https://opensource.org/license/apache-2-0)

`jsoniq-jupyter-lsp` is a Python package that provides a language server setup for the JSONiq programming language. This package includes the necessary configuration to enable JSONiq to work seamlessly with the JupyterLab LSP (`jupyterlab-lsp`) extension, offering rich language features to users of JupyterLab.

## Features

- **Language Server for JSONiq**: Ships the JSONiq Language Server to provide language features following the LSP.
- **JupyterLab Integration**: Configures JupyterLab to recognize and use the JSONiq language server through the `jupyterlab-lsp` extension.
- **Rich Language Features**: Provides auto-completion and diagnostics for JSONiq in JupyterLab.

## Installation

You can install the `jsoniq-jupyter-lsp` package using pip:

```bash
pip install jsoniq-jupyter-lsp
```

## Usage

To use the JSONiq language server in JupyterLab, follow these steps:

1. **Install JupyterLab and the JupyterLSP extension**:

   ```bash
   pip install jupyterlab jupyterlab-lsp
   ```

2. **Install the `jsoniq-jupyter-lsp` package**:

   ```bash
   pip install jsoniq-jupyter-lsp
   ```

3. **Install the `jsoniq-jupyter-extension`** (Needed to recognize magic cells with `%%jsoniq` within Python Notebook cells):

   ```bash
   npm install jsoniq-jupyterlab-extension && jupyter labextension enable jsoniq-jupyterlab-extension
   ```

4. **Start JupyterLab**:

   ```bash
   jupyter lab
   ```

## Configuration

By default, `jsoniq-jupyter-lsp` will be automatically configured to work with JupyterLab. However, you may need to enable auto-completion for the `jupyterlab-lsp` if not enabled. For this, you should go through the following steps:

1. Open Settings
2. Select 'Code Completion'
3. Enable the 'auto_completion' option field.

## Contributing

We welcome contributions to the `jsoniq-jupyter-lsp` project! If you have any suggestions, bug reports, or pull requests, please feel free to submit them on the [GitHub repository](https://github.com/RumbleDB/jsoniq-jupyterlab-lsp).

### Development Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/RumbleDB/jsoniq-jupyterlab-lsp.git
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
