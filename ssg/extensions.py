import sys, importlib
from pathlib import Path

def load_module(directory,name):

    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)

def load_directory(directory):
    for path in directory.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)

def load_bundled():
    directory = Path("/home/work/Documents/vs_code_projects/python-extensions-static-site-generator/python-extensions-static-site-generator/ssg/extensions").parent
    
    load_directory(directory)




print(type(sys.path))
