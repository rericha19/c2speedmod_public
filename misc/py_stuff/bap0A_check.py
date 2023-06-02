# python bap0A_check.py C:\Users\samo1\Desktop\C2_scalemod

# for checking that all levels with smodc also have bap0A

from pathlib import Path
import sys
import array

if (len(sys.argv) < 2):
    print("missing path")
    sys.exit(1)

def eid_conv(m_value):
    charset = "0123456789" + \
    "abcdefghijklmnopqrstuvwxyz" + \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
    "_!"

    temp = ""
    temp += charset[(m_value >> 25) & 0x3F]
    temp += charset[(m_value >> 19) & 0x3F]
    temp += charset[(m_value >> 13) & 0x3F]
    temp += charset[(m_value >> 7) & 0x3F]
    temp += charset[(m_value >> 1) & 0x3F]
    return temp


outstring = ""
for p in Path(sys.argv[1]).rglob('*'):
    if str(p).endswith('.NSD') and p.is_file():
        has_smodc = False
        has_bap0a = False
        with open(p.absolute(), 'rb') as file:
            data = file.read()
            word_array = array.array('I')
            word_array.frombytes(data)
            for word in word_array:
                eid = eid_conv(word)
                if eid == 'SModC':
                    has_smodc = True
                if eid == 'bap0A':
                    has_bap0a = True
        if has_smodc and not has_bap0a:
            print(p.name)

print(outstring)
