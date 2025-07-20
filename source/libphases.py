# Module for logic stuff
from pathlib import Path
from subprocess import run

def checkDirectory(strRoute:str):
    route=Path(f"{strRoute}")
    return route.is_dir()
    
def createDirectory(route:str):
    run(["mkdir", "-p", route])