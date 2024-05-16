import setuptools

setuptools.setup(
    name="jupyter-lsp-jsoniq-language-server",
    version="1.0.0",
    description="Jupyter extension to support RumbleDB development in notebooks. The extension runs the language server for JSONiq to provide code auto-completion, syntax highlighting, and diagnostics.",
    url="https://www.jsoniq.org/",
    author="David-Marian Buzatu",
    author_email="davidm.buzatu@gmail.com",
    license="Apache License 2.0",
    keywords="rumble jsoniq rumbledb json IPython jupyter",
    py_modules=["jupyter-lsp-jsoniq-language-server"],
    entry_points={
        "jupyter_lsp_spec_v1": [
            "jupyter-jsoniq-language-server = src.jsoniq_spec:jsoniq"
        ],
        "console_scripts": ["jsoniq-lsp = src.jsoniq_spec:main"],
    },
    classifiers=[
        # Intended Audience.
        "Intended Audience :: Developers",
        # Operating Systems.
        "Operating System :: OS Independent",
    ],
    install_requires=["jupyter"],
)
