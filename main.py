import create_bytes
import channel
import recv_data


def run(num_bytes, block_size, S_dev):
    # num_bytes = int(input("Number of Bytes : "))
    # block_size = int(input("Block size : "))
    # S_dev = float(input("Standard Deviation : "))

    big_data = create_bytes.create_bytes(num_bytes)
    chunked_data = create_bytes.chunking_data(big_data, block_size)
    parity_pos = create_bytes.find_parity_pos(block_size)
    print "Creating ripe Data ..."
    ripe_data = create_bytes.add_parity_to_data(chunked_data, parity_pos)
    print "Data ready for transfer !"
    # Data ready for transfer
    print "Transferring ..."
    noisy_data = channel.put_noise_on_data(ripe_data, S_dev)

    # Data received
    print "Receiving ..."
    check = recv_data.check_data(noisy_data)

    #
    #
    #
    #

    mistakes = 0
    for i in range(len(check)):
        if check[i] != ripe_data[i]:
            mistakes += 1

    #print mistakes , "errors out off ", num_bytes*8 / block_size

    return mistakes


