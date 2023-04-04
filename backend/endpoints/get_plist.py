import json
import logging
import os
import plistlib
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import Config

class Get_Plist:
    output = dict()
    output["docsets"] = []


    def find_plist(path):
        with os.scandir(path) as it:
            for entry in it:
                docset_root = os.path.join(path, entry.name)
                plist_path = os.path.join(docset_root, "Contents", "Info.plist")
                if(os.path.isfile(plist_path)):
                    if(Get_Plist.parse_plist(plist_path)):
                        Get_Plist.output["docsets"][-1]["docset_root"] = docset_root
                        for f in ["icon.png", "icon@2x.png"]:
                            if os.path.isfile(os.path.join(docset_root, f)):
                                Get_Plist.output["docsets"][-1][f] = os.path.join(docset_root, f)


    def parse_plist(path):
        # TODO figure out all possible fields
        fields = [
                "CFBundleIdentifier", 
                "CFBundleName", 
                "DocSetPlatformFamily"]

        with open(path, "rb") as fp:
            pl = plistlib.load(fp)

        if "isDashDocset" in pl and not pl["isDashDocset"]:
            return False

        Get_Plist.output["docsets"].append({})
        for f in fields:
            Get_Plist.output["docsets"][-1][f] = pl[f]

        return True


    def main():
        if not os.path.isdir(Config.docset_base):
            e = "Invalid DOCSET_BASE \"" + Config.docset_base + "\""
            logging.error(e);
            Get_Plist.output["success"] = False
            Get_Plist.output["message"] = e

        else:
            Get_Plist.find_plist(Config.docset_base);
            Get_Plist.output["success"] = True

        return json.dumps(Get_Plist.output)

if __name__ == "__main__":
    Get_Plist.main()
