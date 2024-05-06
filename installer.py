import os
import json

#JSON export
def savejson(json):
    with open('options.json', 'w') as f:
        f.write(str(json).replace("'", '"').replace("True", "true").replace("False", "false"))
def environmentconversion(env):
  if env == "0":
    return "KDE Plasma (Heavy)"
  elif env == "1":
    return "XFCE4 (Lightweight)"
  elif env == "2":
    return "I3 (Very Lightweight)"
  elif env == "3":
    return "GNOME 42 (Very Heavy)"
  elif env == "4":
    return "Cinnamon"
  elif env == "5":
    return "LXQT"
  else:
    return env
defaultjson = {"defaultapps": [], "programming": [], "apps": [], "enablekvm": True, "DE": "KDE Plasma (Heavy)"}
data = defaultjson
wine = input("Do you want to install wine? (Y/n)")
brave = input("Do you want to install brave? (Y/n)")
xarchiver = input("Do you want to install Xarchiver? (Y/n)")
if not wine == "n":
  data["defaultapps"].append(0)
if not brave == "n":
  data["defaultapps"].append(1)
if not xarchiver == "n":
  data["defaultapps"].append(2)
environment = input("""
Which environment do you want:
KDE Plasma (Heavy) : 0
XFCE4 (Lightweight) : 1
I3 (Very Lightweight) : 2
GNOME 42 (Very Heavy) : 3
Cinnamon : 4
LXQT : 5
""")
environment = environmentconversion(environment)
data["DE"] = environment
savejson(data)
