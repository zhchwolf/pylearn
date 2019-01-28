#!/usr/bin/env python3
# coding:utf-8

import sys
import os
import glob
import csv
# import pandas
# import xlrd
# import xlwt
from xlrd import open_workbook
from xlwt import Workbook
'''
xlrd and xlwt is work for xls file, not xlsx file.
'''

# self_file = sys.argv[0]
input_file = sys.argv[1]
output_file = sys.argv[2]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:",worksheet.ncols)

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("2012_EN_out")
with open_workbook(input_file) as open_wb:
    ws = open_wb.sheet_by_name("2012_EN")
    for row_index in range(ws.nrows):
        for column_index in range(ws.ncols):
            output_worksheet.write(row_index,column_index,ws.cell_value(row_index,column_index) )
output_workbook.save(output_file)

