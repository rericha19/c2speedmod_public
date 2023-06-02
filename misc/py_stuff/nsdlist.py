# python nsdlist.py C:\Users\samo1\Desktop\C2_scalemod

# used to list all nsd files and create a copy/paste-able text for c2export
# was used to determine which gool type is available in all levels

from pathlib import Path
import sys
if (len(sys.argv) < 2):
    print("missing path")
    sys.exit(1)

outstring = ""
for p in Path(sys.argv[1]).rglob('*'):
    if str(p).endswith('.NSD') and p.is_file():
        outstring += "nsd {}\n".format(str(p))

print(outstring)
