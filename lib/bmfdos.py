import os
import sys

def osclear():
    systemos = os.name

    if systemos == "nt":
        os.system("cls")
    elif systemos == "posix":
        os.system("clear")

def launchPythonConfigFile(name):
    systemos = os.name

    if systemos == "nt":
        os.system(f"py {name}.py")
    elif systemos == "posix":
        os.system(f"python {name}.py")