import sys
import os.path
from utils import *


def decompress(file):
    name, ext = os.path.splitext(file)

    if ext != ".asco":
        raise ValueError(f"Expected .asco file, got {ext} instead")

    # Open the specified file in binary mode and create a new TXT file
    with open(file, "rb") as rf, open(f"{name}_decompressed.txt", "wb") as wf:
        sig = rf.read(4)

        if sig != SIGNATURE:
            raise Exception("Bad file signature")

        bytemap = dict()
        sequence = bytes()
        key = rf.read(1)

        while (byte := rf.read(1)):
            if key == NULL:
                wf.write(bytemap[byte] + SPACE)
            else:
                if byte == NULL:
                    bytemap[key] = sequence
                    sequence = bytes()
                    key = rf.read(1)
                else:
                    sequence += byte


if __name__ == "__main__":
    decompress(sys.argv[1])
