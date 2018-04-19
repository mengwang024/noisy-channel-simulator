import random,math

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
    r = 1
    while do:
        r += 1
        if block_size + r < 2 ** r:
            do = False

    parity_nums = r
    parity_pos = []

    for i in range(parity_nums):
        parity_pos.append(2 ** i - 1)

    # parity pos are ready !
    return parity_pos


def create_parity(parity_pos, full_data):
    mstr = ''
    new_data = []
    for i in range(len(full_data)):
        if i in parity_pos:
            new_data.append("0")
        else:
            new_data.append(full_data[len(full_data) - 1 - i])

    for pos in parity_pos:

        xor = 0
        for i in range(len(full_data)):

            leni = len(bin(i + 1))
            if bin(i + 1)[leni - 1 - int(math.log(pos+1, 2))] == '1':

                xor = xor ^ int(full_data[len(full_data) - 1 - i])

        new_data[pos] = xor

    for i in range(len(new_data)):
        mstr = str(new_data[i]) + mstr

    return mstr


def add_parity_to_data(chunked_data, parity_pos):
    ripe_data = []

    for data in chunked_data:
        full_data = ""
        for i in range(len(data) + len(parity_pos)):
            if i in parity_pos:
                full_data = '0' + full_data
            else:
                if len(data) - 1 != -1:
                    full_data = data[len(data) - 1] + full_data
                    data = data[:len(data) - 1]

        ripe_data.append(create_parity(parity_pos, full_data))

    return ripe_data
