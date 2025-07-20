# Module for logic stuff
from pathlib import Path
from subprocess import run

def checkDirectory(strRoute):
    route=Path(f"{strRoute}")
    if route.is_dir():
        run(["mkdir"," -p", "strRoute"])
    else:
        pass