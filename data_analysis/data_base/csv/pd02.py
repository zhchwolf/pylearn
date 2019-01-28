#!/usr/bin/env python3
# --coding:utf8---

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
important_dates = ['2004','2005']
data_frame_value_in_set = data_frame.loc[data_frame['Date'].isin(important_dates),:]
data_frame_value_in_set.to_csv(output_file,index=False)

