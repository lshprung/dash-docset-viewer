import json
import logging
import os
import plistlib
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import Config

output = dict()
output["paths"] = []

def find_plist(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.name == "." or entry.name == ".." or entry.name == "Resources":
                continue
            if(os.DirEntry.is_dir(entry)):
                find_plist(path + "/" + entry.name)
            elif(entry.name == "Info.plist"):
                #parse_plist(path + "/" + entry.name)
                output["paths"].append(path + "/" + entry.name)

def parse_plist(path):
    with open(path, "rb") as fp:
        pl = plistlib.load(fp)
    print(pl["CFBundleIdentifier"])
    print(pl["CFBundleName"])



if not os.path.isdir(Config.docset_base):
    e = "Invalid DOCSET_BASE \"" + Config.docset_base + "\""
    logging.error(e);
    output["success"] = False
    output["message"] = e

else:
    find_plist(Config.docset_base);
    output["success"] = True

print(json.dumps(output))
