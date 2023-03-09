import os

x = input("plugin:")
res = ""
print("Packing plugin...")
for i in os.listdir("plugins/"+x):
    if i != x+".par":
        res += f"<--File:{i}\n"
        with open("plugins/"+x+"/"+i) as fl:
            res += fl.read()
        res += "\n"
with open("plugins/"+x+"/"+x+".par", "w") as fl:
    fl.write(res)
print("Plugin packed!")