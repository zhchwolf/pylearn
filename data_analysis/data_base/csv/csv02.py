#!/usr/bin/env python3
# --coding:utf8---

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            x_date = str(row_list[3]).strip()
            cost = str(row_list[1]).replace(',','')
            if x_date[-3:] == 'Jan' or float(cost) <= 0.001:
                filewriter.writerow(row_list)