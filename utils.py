SIGNATURE = b"asco"
SPACE = b"\x20"
NULL = b"\x00"


def write_key(file, key, bytemap):
    # Assign unique keys in the bytemap beginning at 0x01
    if key not in bytemap:
        bytemap[key] = len(bytemap) + 1
        file.write(bytes([len(bytemap)]) + key + NULL)
