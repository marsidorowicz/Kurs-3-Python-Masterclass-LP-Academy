# file_1 = open("e:\\original.txt", 'r')
#
# for line in file_1:
#     if "jabberwock" in line.lower():
#         print(line, end="")
# file_1.close()
# with open("e:\\original.txt", 'r') as file_1:
#     for line in file_1:
#         if "JAB" in line.upper():
#             print(line, end="")
# with open("e:\\original.txt", 'r') as file_1:
#     line = file_1.readline()
#     while line:
#         print(line, end="")
#         line = file_1.readline()
with open("e:\\original.txt", 'r') as file_1:
    lines = file_1.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end="")