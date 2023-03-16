# đọc file txt
def docFile():
    file = open('input',encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()

with open('input', 'r') as f:
    numbers = f.read().split()
so_chan = 0
so_le = 0
for num in numbers:
    if int(num) % 2 == 0:
        so_chan += 1
    else:
        so_le += 1
docFile()
print(f"Số lượng số chẵn là: {so_chan}")
print(f"Số lượng số lẻ là: {so_le}")



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

so_nguyen_to = 0

for num in numbers:
    if is_prime(int(num)):
        so_nguyen_to += 1

print(f"Số lượng số nguyên tố là: {so_nguyen_to}")


number_count = {}
max_count = 0
most_common = None

for num in numbers:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1

for num, count in number_count.items():
    if count > max_count:
        max_count = count
        most_common = num

print(f"Số xuất hiện nhiều nhất là: {most_common}, xuất hiện {max_count} lần")


# from openpyxl import load_workbook
# wb = load_workbook('input.xlsx')
# print(wb.sheetnames)
# ws = wb[wb.sheetnames[0]]
# for row in ws.values:
#     for value in row:
#         print(value,"\t", end = '')
#     print("")