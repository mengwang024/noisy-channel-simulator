import math, numpy


def put_noise_on_data(ripe_data, zarib):
    recv_data = []

    for data in ripe_data:

        len = len(data)

        new_data = ""

        for i in range(len(data)):
            Random = numpy.random.randn(1, len(data)) * zarib

            data[i] = float(data[i]) + Random[i]

            if data[i] > 0.5:
                data[i] = 1
            else:
                data[i] = 0

        new_data = data
        recv_data.append(new_data)

    return recv_data
