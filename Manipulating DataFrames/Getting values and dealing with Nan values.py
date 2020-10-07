# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np #Nan

data = {"Part 1":[1,2,3,4,5,np.nan],
        "Part 2":[5,4,3,2,1,np.nan],
        "Part 3":[1,9,2,8,3,np.nan],
        "Nan Part":[4,3,np.nan,1,2,np.nan,]
        }
newIndex = ["A","B","C","D","E","F"]

df = pd.DataFrame(data,index = newIndex)

print(df)

#val = #
print("Getting value:",df._get_value("A","Part 2"))

for index,series in df.iterrows():
    print(series["Part 2"])


print("Checking if there are any NaN values\n", df.isnull())
print(df.notnull())

#print(df.dropna(0,'any'))
#print(df.dropna(0,'all))
print(df.dropna(1, thresh = 5))
