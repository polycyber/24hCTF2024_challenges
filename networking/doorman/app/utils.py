import ipaddress

def xor(a: bytes, b: bytes):
    i = 0
    out = bytearray()
    out_size = max(len(a), len(b))

    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a

    while len(out) != out_size:
        out.append(a[i % len(a)] ^ b[i % len(b)])
        i += 1

    return bytes(out)

def is_ip_address(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False