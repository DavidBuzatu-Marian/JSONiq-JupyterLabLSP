def load(app):
    return {
        "jsoniq-language-server": {
            "version": 2,
            "argv": ["jsoniq-lsp-start"],
            "languages": ["jsoniq"],
            "mime_types": [
                "application/jsoniq",
                "text/python",
                "text/x-python",
                "application/x-ipynb+json",
            ],
        }
    }
