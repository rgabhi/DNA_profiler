import csv
from sys import*
import re

# check if valid input format
if len(argv) < 3:
    print("wrong format")
    exit(0)

fields = []  # headings
rows = []  # data

# read user-dna data
with open(argv[1], 'r') as dnafile:
    csvreader = csv.reader(dnafile)

    # field names in first row
    fields = next(csvreader)

    # extract str data
    for row in csvreader:
        rows.append(row)

# for row in rows:
#     for col in row:
#         print(col, end = " ")
#     print("\n")

# read sequence string
with open(argv[2], 'r') as sequencefile:
    data = sequencefile.read()

str_cnts = []
match = False
# print(data)
for pattern in fields[1:]:
    max_occurence = max(re.findall('((?:' + re.escape(pattern) + ')*)', data), key=len)
    cnt = len(max_occurence) // len(pattern)
    str_cnts.append(cnt)

# TEST
# for cnt in str_cnts:
#     print(cnt, end= ", ")
# print("\n")

n = len(rows)
m = len(rows[0])

for i in range(n):
    match = True
    for j in range(1, m):
        if str_cnts[j - 1] != int(rows[i][j]):
            # print(f"different: {rows[i][0]} => {str_cnts[j]} (type: {type(str_cnts[j])}), {rows[i][j + 1]} (type : {type(rows[i][j + 1])})")
            match = False
            break
    if match:
        print(rows[i][0])
        break
# NO match found
if match == False:
    print("No match")

exit(1)