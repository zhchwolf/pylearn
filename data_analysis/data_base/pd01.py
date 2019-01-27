#!/usr/bin/env python3
# --coding:utf8---

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame['Y-Mbyte'] = data_frame['Y-Mbyte'].str.replace(',','').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Month'].str.contains('Jan')) | (data_frame['Y-Mbyte'] < 0.001 ),:]
data_frame_value_meets_condition.to_csv(output_file,index=False)

