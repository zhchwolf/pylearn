#!/usr/bin/env python3
# --coding:utf8---

import csv
import sys
import re

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^N.*)',re.I)
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            company_name = row_list[6]
            if pattern.search(company_name):
                filewriter.writerow(row_list)
