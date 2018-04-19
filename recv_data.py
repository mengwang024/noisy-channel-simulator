import math


# Todo : have to correct this code


def check_data(recv_data):
    pure_data = []
    parity_pos = []


    block_size = len(recv_data[0])
    parity_num = int(math.floor(math.log(block_size, 2)) + 1)
    for i in range(parity_num):
        a = 2 ** i - 1
        parity_pos.append(a)

    for data in recv_data:
        mstr = ''
        new_data = []
        xor_ans = []
        for i in range(len(data)):
            new_data.append(data[len(data) - 1 - i])

        for pos in parity_pos:

            xor = 0
            for i in range(len(data)):

                leni = len(bin(i + 1))
                if bin(i + 1)[leni - 1 - int(math.log(pos + 1, 2))] == '1':
                    xor = xor ^ int(data[len(data) - 1 - i])

                    # if xor == 1 :
                    # new_data[pos] = data[len(data)-1-pos]

            xor_ans.append(xor)

        pos_problem = ''
        for i in xor_ans:
            pos_problem = str(i) + pos_problem

        pos_problem = int(pos_problem,2) - 1

        if pos_problem > 0 :

            if new_data[pos_problem] == "0":
                new_data[pos_problem] = '1'
            else :
                new_data[pos_problem] = '0'

        for i in range(len(new_data)):
            mstr = str(new_data[i]) + mstr
        pure_data.append(mstr)

    return pure_data

