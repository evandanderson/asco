import sys
import os.path
from utils import *


def compress(file):
    name, ext = os.path.splitext(file)

    if ext != ".txt":
        raise ValueError(f"Expected .txt file, got {ext} instead")

    # Open the specified file in binary mode and create a new ASCO file
    with open(file, "rb") as rf, open(f"{name}.asco", "wb") as wf:
        bytemap = dict()
        sequence = bytes()
        data = bytes()

        wf.write(SIGNATURE)
        while (byte := rf.read(1)):
            if byte.isspace():
                write_key(wf, sequence, bytemap)
                data += bytes([bytemap[sequence]])
                sequence = bytes()
            else:
                sequence += byte

        write_key(wf, sequence, bytemap)
        data += bytes([bytemap[sequence]])
        wf.write(NULL + data)


if __name__ == "__main__":
    compress(sys.argv[1])
