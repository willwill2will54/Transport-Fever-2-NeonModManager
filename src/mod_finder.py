import os, re

from Mod import Mod

from helpfunctions import *

def getExternalMod(folder):

    mod_lua = open(os.path.join(folder, "mod.lua"), "r", encoding="utf-8")

    mod_lua_text = mod_lua.read()
    x = re.search("name.*=.*_.*,", mod_lua_text)
    if x:
        name = x.group()[10: len(x.group())-3]
    else:
        x = re.search("name.*=.*,", mod_lua_text)
        name = x.group()[9: len(x.group())-3]

    x = re.search("minorVersion.*=.*,", mod_lua_text)
    if x:
        x = x.group()[11: len(x.group())-1]
        minorVersion = int(re.findall("[0-9]", x)[0])
    else:
        minorVersion = None

    x = re.search("tfnetId.*,", mod_lua_text)
    if x:
        source = "transportfever.net"
    else:
        source = "other"

    try:
        image = open(os.path.join(folder,"workshop_preview.jpg"), "r")
    except:
        image = None

    return Mod(name, minorVersion, source, image)
def getExternalMods(externalModsDirectory):
    folders = os.listdir(externalModsDirectory)

    try:
        folders.remove("readme.txt")
    except:
        pass
    Mods = []
    for folder in folders:
        Mods.append(getExternalMod(os.path.join(externalModsDirectory, folder)))
    return Mods

def getSteamMod(folder):
    mod_lua = open(os.path.join(folder, "mod.lua"), "r", encoding="utf-8")

    mod_lua_text = mod_lua.read()
    x = re.search("name.*=.*_.*,", mod_lua_text)
    if x:
        name = x.group()[10: len(x.group())-3]
    else:
        x = re.search("name.*=.*,", mod_lua_text)
        name = x.group()[9: len(x.group())-3]

    x = re.search("minorVersion.*=.*,", mod_lua_text)
    if x:
        x = x.group()[11: len(x.group())-1]
        minorVersion = int(re.findall("[0-9]", x)[0])
    else:
        minorVersion = None

    source = "Steam"

    try:
        image = open(os.path.join(folder,"workshop_preview.jpg"), "r")
    except:
        image = None

    return Mod(name, minorVersion, source, image)
def getSteamMods(steamModsDirectory):
    folders = os.listdir(steamModsDirectory)

    try:
        folders.remove("readme.txt")
    except:
        pass
    Mods = []
    for folder in folders:
        Mods.append(getSteamMod(os.path.join(steamModsDirectory, folder)))
    return Mods
