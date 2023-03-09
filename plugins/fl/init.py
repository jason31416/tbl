from lib import *
import os

try:
    getdt("_test")
except Exception:
    def setdt(a, b):
        pass
    def getdt(a):
        pass
    def run_command(a):
        pass
    usr = "local"
    tbl_print("Running in local mode!")

tbl_print("&3mLoading file system...")

setdt("curdir", "")

if not os.path.exists("files"):
    os.mkdir("files")

tbl_print("&3mLoaded file system!")