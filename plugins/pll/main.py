from lib import *
import os
import requests

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
    exit(0)

if len(args) == 0:
    tbl_print("&1mUnknown command&7m!")
elif args[0] == "list":
    tbl_print("&3mList of plugins:")
    for i in os.listdir("plugins"):
        tbl_print("&7m- &3m"+i)
elif args[0] in ["rm", "remove"]:
    if len(args) == 1:
        tbl_print("&1mMissing argument!")
    elif os.path.exists("plugins/"+args[1]):
        tbl_print(f"&1mAre you sure about removing the plugin: {args[1]}(WILL REMOVE ALL DATAS STORED LOCALLY!)")
        if tbl_input("(y/n):") == "y":
            os.rmdir("plugins/"+args[1])
            tbl_print(f"&2mSuccessfully removed '{args[1]}'!")
    else:
        tbl_print(f"&1mPlugin '{args[1]}' doesn't exist!")
elif args[0] in ["install", "is"]:
    if len(args) == 1:
        tbl_print("&1mMissing argument!")
    elif os.path.exists("plugins/"+args[1]):
        tbl_print(f"&1mPlugin exists!")
    else:
        tbl_print(f"&3mDownloading files...")
        if ct[:4] == "git:":
            ct = requests.get(
                "https://raw.githubusercontent.com/" + args[1]).content.decode(
                "utf-8")
        elif ct[:4] == "web:":
            ct = requests.get(args[1]).content.decode(
                "utf-8")
        else:
            ct = requests.get("https://raw.githubusercontent.com/jason31416/tbl_plugins/main/"+args[1]+".par").content.decode("utf-8")

        if ct == "404: Not Found":
            tbl_print(f"&1mPlugin doesn't exist!")
        else:
            tbl_print(f"&3mInstalling package...")
            os.mkdir("plugins/"+args[1])
            cur = ""
            curfl = ""
            for i in ct.split("\n"):
                if i[:8] == "<--File:":
                    if curfl != "":
                        with open(f"plugins/{args[1]}/{curfl}", "w") as fl:
                            fl.write(cur)
                    curfl = i[8:]
                    cur = ""
                else:
                    cur += i+"\n"
            if curfl != "":
                with open(f"plugins/{args[1]}/{curfl}", "w") as fl:
                    fl.write(cur)
            tbl_print(f"&2mSuccessfully installed '{args[1]}'!")

else:
    tbl_print("&1mUnknown command&7m!")




