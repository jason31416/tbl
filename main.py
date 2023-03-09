import typing
import os

import utlogin
from lib import *

welcome = ["&4mWelcome to the &2mtextOS&7m!"]

dt = {}

loginsysip = "spacesmc.cn"

def setdt(ky, vl):
    dt[ky] = vl

def getdt(ky):
    if ky in dt:
        return dt[ky]
    return ""

def runcmd(cmd: str):
    if cmd.split(" ")[0] in pl:
        pl[cmd.split(" ")[0]].run(cmd.split(" ")[1:])
        return True
    return False

class plugin:
    def __init__(self, cd, init):
        self.cd = cd
        self.ini = init
        self.hp = []
    def run(self, args):
        try:
            exec(self.cd, globals(), {"args": args, "setdt": setdt, "getdt": getdt, "run_command": runcmd, "getremotedt": utlogin.getdt, "setremotedt": utlogin.setdt})
        except Exception as e:
            raise e
            # tbl_print(f"&1mError:\n{e}")

placeholders: typing.List[placeholder] = []

tbl_print(welcome)
utlogin.init(loginsysip)
while True:
    tbl_print("&4mLogin:")
    usr = tbl_input("&6mUsername:")
    psw = tbl_input("&6mPassword:")

    ret = utlogin.login(usr, psw)

    if ret[0] == "success":
        tbl_print("&2mSuccess&7m!")
        break
    elif ret[0] == "usrnotexist":
        tbl_print("&1mUser doesn't exist&7m!")
        if tbl_input("&6mRegister instead&7m?&6m (y/n): ") == "y":
            ret = utlogin.register(usr, psw)
            if ret == "success":
                ret = utlogin.login(usr, psw)
                if ret[0] == "success":
                    tbl_print("&2mSuccessfully registered&7m!")
                    break
                else:
                    tbl_print(f"&1mInternal server error occored: Unknown return code: &2m{ret[0]}&7m!")
                    exit(0)
            else:
                tbl_print(f"&1mInternal server error occored: Unknown return code: &2m{ret}&7m!")
                exit(0)
    elif ret[0] == "wrongpsw":
        tbl_print("&1mPassword is incorrect&7m!")
    else:
        tbl_print(f"&1mInternal server error occored: Unknown return code: &2m{ret}&7m!")
        exit(0)

def read_file(fl):
    with open(fl) as fll:
        return fll.read()

tbl_print("&3mLoading plugins...")

pl = {}

for i in os.listdir("plugins"):
    if os.path.isdir("plugins/"+i):
        if os.path.exists("plugins/"+i+"/main.py"):
            if os.path.exists("plugins/" + i + "/init.py"):
                pl[i] = plugin(read_file("plugins/" + i + "/main.py"), read_file("plugins/" + i + "/init.py"))
            else:
                pl[i] = plugin(read_file("plugins/" + i + "/main.py"), "")
            if os.path.exists("plugins/" + i + "/help.txt"):
                pl[i].hp = read_file("plugins/" + i + "/help.txt").split("\n")


for i in pl:
    try:
        exec(pl[i].ini, globals(), {"setdt": setdt, "getdt": getdt, "run_command": runcmd, "user": usr, "getremotedt": utlogin.getdt, "setremotedt": utlogin.setdt})
    except Exception as e:
        tbl_print(f"&1mError:\n{e}")


tbl_print("&3mPlugins loaded!")


tbl_print("&4mMain menu(h for help):")

while True:
    inp = tbl_input("&6m>>").split(" ")
    if inp[0] in pl:
        pl[inp[0]].run(inp[1:])
    elif inp[0] in ["h", "help"]:
        tbl_print("&3mHelps:")
        for i in pl:
            if len(pl[i].hp)==0:
                break
            tbl_print(f"&7m- &3m{i}:")
            for j in pl[i].hp:
                tbl_print("  "+j)
        tbl_print("&3mexit/quit/stop to quit")
        tbl_print("&3mreload to reload all plugins")
    elif inp[0] in ["exit", "quit", "stop"]:
        tbl_print(f"&4mBye!")
        exit(0)
    elif inp[0] == "reload":
        tbl_print("&3mLoading plugins...")

        pl = {}
        dt = {}

        for i in os.listdir("plugins"):
            if os.path.isdir("plugins/" + i):
                if os.path.exists("plugins/" + i + "/main.py"):
                    if os.path.exists("plugins/" + i + "/init.py"):
                        pl[i] = plugin(read_file("plugins/" + i + "/main.py"), read_file("plugins/" + i + "/init.py"))
                    else:
                        pl[i] = plugin(read_file("plugins/" + i + "/main.py"), "")
                    if os.path.exists("plugins/" + i + "/help.txt"):
                        pl[i].hp = read_file("plugins/" + i + "/help.txt").split("\n")

        for i in pl:
            try:
                exec(pl[i].ini, globals(),
                     {"setdt": setdt, "getdt": getdt, "run_command": runcmd, "user": usr, "getremotedt": utlogin.getdt,
                      "setremotedt": utlogin.setdt})
            except Exception as e:
                tbl_print(f"&1mError:\n{e}")

        tbl_print("&3mPlugins loaded!")
    else:
        tbl_print(f"&1mError: Unknown command &3m{inp[0]}&1m!")