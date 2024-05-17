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
        / "server.js"
    ).resolve()
)


def main():
    # Run the language server
    print("Starting language server...")
    server_proc = subprocess.Popen(
        [NODE, PATH_TO_BIN_JS, "--stdio", *sys.argv[1:]],
        stdin=sys.stdin,
        stdout=sys.stdout,
    )
    print("Running language server...")
    sys.exit(server_proc.wait())


if __name__ == "__main__":
    main()
