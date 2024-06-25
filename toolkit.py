import struct


def float_to_bytes(f: float) -> bytes:
    b = struct.pack("f", f)
    return b


def bytes_to_float(bs: bytes) -> float:
    return struct.unpack("f", bs)[0]


def log(msg: str) -> None:
    fp = "/logs"
    f = open(fp, "a")
    f.write(msg + "\n\n")
    f.close()
