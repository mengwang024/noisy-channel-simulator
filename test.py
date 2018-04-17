data = "asdfg"
parity_pos = [7,3,1,0]
raw = ""
for i in range(len(data) + len(parity_pos)):
    if i in parity_pos:
        raw = str(i) + raw
    else:
        raw = data[len(data) - 1] + raw
        data = data[:len(data) - 1]


print raw