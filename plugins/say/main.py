from lib import *
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

tbl_print(" ".join(args))