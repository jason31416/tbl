placeholders = []

class placeholder:
    def __init__(self, txt, valfunc = None, val=""):
        def deffunc():
            return val
        self.txt = txt
        if valfunc is None:
            valfunc = val
        self.func = valfunc

def _replace(txt: str):
    for i in placeholders:
        txt = txt.replace(i.txt, i.func())
    txt = txt.replace("&&", "<-TEMP!->").replace("&", "\033[3").replace("<-TEMP!->", "&")+"\033[0m"
    return txt

def tbl_print(txt, end="\n"):
    if type(txt) == str:
        print(_replace(txt), end=end)
    else:
        print(_replace("\n".join(txt)), end=end)

def tbl_input(txt, tp=str):
    return tp(input(_replace(txt)))