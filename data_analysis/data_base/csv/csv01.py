#!/usr/bin/env python3
# --coding:utf8---

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# with open(input_file,'r',newline='') as filereader:
#     with open(output_file,'w',newline='') as filewriter:
#         header = filereader.readline()
#         header = header.strip()
#         header_list = header.split(',')
#         print(header_list)
#         filewriter.write(','.join(map(str,header_list))+'\n')
#         for row in filereader:
#             row = row.strip()
#             row_list = row.split(',')
#             print(row_list)
#             filewriter.write(','.join(map(str,row_list))+'\n')

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=',')
        filerwriter = csv.writer(csv_out_file,delimiter=',')
        for row_list in filereader:
            print(row_list)
            filerwriter.writerow(row_list)
