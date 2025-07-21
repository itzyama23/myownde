# Module for logic stuff
from pathlib import Path
from subprocess import run

def checkDirectory(strRoute:str):
    route=Path(f"{strRoute}")
    return route.is_dir()
    
def createDirectory(route:str):
    run(["mkdir", "-p", route], capture_output=True)

def copyFilesFrom(fromRoute:str=None, toRoute:str=None, sudo:bool=None):
    if sudo is None or sudo is False:
        run(["cp", "-r", fromRoute, toRoute])
    elif sudo is True:
        run(["sudo", "cp", "-r", fromRoute, toRoute])
    else:
        pass
    return True