def strToBytes(s: str) -> bytes:
    size = bytes(len(s).to_bytes(2, byteorder='little'))
    data = bytes([0xBB, 0xAA]) + size + bytes(s, encoding='utf-8')
    return data
