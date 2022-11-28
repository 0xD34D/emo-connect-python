CMD_CATEGORY = [0, 1, 2, 3, 4, 5]
CMD_ORDER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
CMD_ORDER_DATA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
CMD_GAME_NUMBER = [1, 2, 3, 4, 5, 6, 7]
sort = 1


def cmd(data: list[int]) -> bytes:
    payload = bytes([0xDD, 0xCC, sort]) + bytes(data)
    return payload


def statusOnOff(on: bool) -> bytes:
    return cmd([CMD_CATEGORY[0], CMD_ORDER_DATA[0], 1 if on else 0])


def chargeLevelOnOff(on: bool) -> bytes:
    return cmd([CMD_CATEGORY[2], CMD_ORDER_DATA[0], 1 if on else 0])
