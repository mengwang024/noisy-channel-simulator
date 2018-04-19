import main
import xlsxwriter


row = 0
col = 0

excel = [["Lab", 'num_bytes', 'block_size', 'S_dev', 'mistakes', 'Total Blocks']]
lab = 1
con = 1
while (con):
    num_bytes = int(input("Number of Bytes : "))
    block_size = int(input("Block size : "))
    S_dev = float(input("Standard Deviation : "))
    mistake = main.run(num_bytes, block_size, S_dev)

    excel.append(["Lab " + str(lab), num_bytes, block_size, S_dev, mistake, num_bytes*8//block_size])
    lab += 1
    con = int(input("Continue ? y/n  "))

    if con == 1:
        pass
    else :
        con = 0

workbook = xlsxwriter.Workbook('Results.xlsx')
worksheet = workbook.add_worksheet()


for line in excel:
    worksheet.write(row, col, line[0])
    worksheet.write(row, col + 1, line[1])
    worksheet.write(row, col + 2, line[2])
    worksheet.write(row, col + 3, line[3])
    worksheet.write(row, col + 4, line[4])
    worksheet.write(row, col + 5, line[5])
    row += 1

workbook.close()
