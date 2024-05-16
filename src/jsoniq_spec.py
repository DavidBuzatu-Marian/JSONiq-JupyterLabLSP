import shutil
import pathlib
import os
import subprocess
import sys

cwd = os.getcwd()

NODE_LOCATION = (
    shutil.which("node") or shutil.which("node.exe") or shutil.which("node.cmd")
)
NODE = str(pathlib.Path(NODE_LOCATION).resolve())
PATH_TO_BIN_JS = str(
    (
        pathlib.Path(__file__).parent
        / "node_modules"
        / "jsoniq-language-server"
        / "dest"
        "server.js"
    ).resolve()
)


def main():
    # Run the language server
    server_proc = subprocess.Popen(
        [NODE, PATH_TO_BIN_JS, "--stdio", *sys.argv[1:]],
        stdin=sys.stdin,
        stdout=sys.stdout,
    )
    sys.exit(server_proc.wait())


def jsoniq(app):
    return {
        "jsoniq-language-server": {
            "version": 2,
            "argv": ["jsoniq-language-server"],
            "languages": ["jsoniq"],
            "mime_types": [
                "text/jsoniq",
                "text/x-jsoniq",
                "text/python",
                "text/x-python",
                "application/x-ipynb+json",
            ],
        }
    }


if __name__ == "__main__":
    main()
