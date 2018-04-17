import random, math


def create_bytes(num_bytes=1000000):
    raw_data = ""

    for i in range(num_bytes * 8):
        rand_bit = str(random.getrandbits(1))

        raw_data += rand_bit

    return raw_data


def chunking_data(raw_data, block_size):
    if raw_data < block_size:
        print "data is less than block size !"
        return -1

    chunked_data = []

    while len(raw_data) > block_size:
        block = raw_data[0:block_size]
        raw_data = raw_data[block_size:]
        chunked_data.append(block)

    if raw_data != "":
        for i in range(block_size - len(raw_data)):
            raw_data += "0"
        chunked_data.append(raw_data)

    return chunked_data


def find_parity_pos(block_size):
    if block_size < 1:
        return -1

    # parity_nums = math.floor(math.log(block_size, 2))
    do = True
    r = 2
    while (do):
        if block_size + 2 < 2 ** r:
            do = False
        r += 1
    parity_nums = r

    parity_pos = []

    while parity_nums >= 0:
        parity_pos.append(2 ** parity_nums - 1)

        parity_nums -= 1

    # parity pos are ready !
    return parity_pos


def add_parity_to_data(chunked_data, parity_pos):
    ripe_data = []

    for data in chunked_data:
        raw = ""
        for i in range(len(data) + len(parity_pos)):
            if i in parity_pos:
                raw = str(i) + raw
            else:
                raw = data[len(data)-1] + raw
                data = data[:len(data) - 1]

        ripe_data.append(raw)

    return ripe_data






