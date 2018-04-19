import numpy


def put_noise_on_data(ripe_data, S_dev):
    recv_data = []

    for str_data in ripe_data:
        data = []

        for i in range(len(str_data)):
            Random = numpy.random.randn(len(str_data)) * S_dev

            if (int(str_data[i]) + Random[i]) > 0.5:
                data.append(1)
            else:
                data.append(0)

        new_data = ''
        for i in data:
            new_data += str(i)
        recv_data.append(new_data)

    return recv_data



