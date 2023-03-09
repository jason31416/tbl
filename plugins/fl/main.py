from lib import *
import os

try:
    xdsa = args
except Exception:
    args = []
    usr = ""
    def setdt(a, b):
        pass
    def getdt(a):
        pass
    def run_command(a):
        pass
    tbl_print("Running in local mode!")

if len(args) == 0:
    tbl_print("&1mUnknown command&7m!")
    setdt("fret", "UnknownCommandError")
elif args[0] == "nw":
    if len(args) == 1:
        tbl_print("&1mMissing argument&7m!")
        setdt("fret", "MissingArgumentError")
    elif os.path.exists("files/"+getdt("curdir")+"/"+args[1]):
        tbl_print("&1mFile already exists&7m!")
        setdt("fret", "FileExistError")
    else:
        open("files/"+getdt("curdir")+"/"+args[1], "w").close()
        setdt("fret", "Success")
elif args[0] == "cd":
    if len(args) == 1:
        setdt("curdir", "")
        setdt("fret", "Success")
    elif os.path.exists("files/"+getdt("curdir")+"/"+args[1]) and os.path.isdir("files/"+getdt("curdir")+"/"+args[1]):
        setdt("curdir", getdt("curdir")+"/"+args[1])
        setdt("fret", "Success")
    else:
        setdt("fret", "DirectoryNotExistError")
elif args[0] == "set":
    if len(args) <= 2:
        tbl_print("&1mMissing argument&7m!")
        setdt("fret", "MissingArgumentError")
    elif os.path.exists("files/"+getdt("curdir")+"/"+args[1]) and os.path.isfile("files/"+getdt("curdir")+"/"+args[1]):
        with open("files/"+getdt("curdir")+"/"+args[1], "w") as fl:
            fl.write(" ".join(args[2:]).replace("\\n", "\n"))
        setdt("fret", "Success")
    else:
        tbl_print("&1mFile doesn't exists&7m!")
        setdt("fret", "FileNotExistError")
elif args[0] == "get":
    if len(args) == 1:
        tbl_print("&1mMissing argument&7m!")
        setdt("fret", "MissingArgumentError")
    elif os.path.exists("files/"+getdt("curdir")+"/"+args[1]) and os.path.isfile("files/"+getdt("curdir")+"/"+args[1]):
        with open("files/"+getdt("curdir")+"/"+args[1]) as fl:
            rd = fl.read()
        tbl_print(rd)
        setdt("fret", rd)
    else:
        tbl_print("&1mFile doesn't exists&7m!")
        setdt("fret", "FileNotExistError")
elif args[0] == "rm":
    if len(args) == 1:
        tbl_print("&1mMissing argument&7m!")
        setdt("fret", "MissingArgumentError")
    elif os.path.exists("files/"+getdt("curdir")+"/"+args[1]):
        os.remove("files/"+getdt("curdir")+"/"+args[1])
        setdt("fret", "Success")
    else:
        tbl_print("&1mFile doesn't exists&7m!")
        setdt("fret", "FileNotExistError")
else:
    tbl_print("&1mUnknown command&7m!")
    setdt("fret", "UnknownCommandError")




