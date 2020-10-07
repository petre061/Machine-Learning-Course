# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:20:00 2020

@author: acer
"""

#Drop rows based on if there are duplicate rows
#Confine our search for duplicates on certain columns
#Drop distinct columns or rows, and using it in a loop

import pandas as pd
import numpy as np #Nan

#data = {"Part 1":[1,2,3,4,1,10,np.nan],
#        "Part 4":[1,2,3,4,1,2,np.nan],
 #       "Part 2":[5,4,3,2,5,10,np.nan],
  #      "Part 3":[1,9,2,8,1,10,np.nan],
   #     "Nan Part":[4,3,np.nan,1,4,3,np.nan]
    #    }
data = {"Part 1":[1,2,3,4,1,10],
        "Part 4":[1,2,3,4,1,2],
        "Part 2":[5,4,3,2,5,10],
        "Part 3":[1,9,2,8,1,10],
        "Nan Part":[4,3,np.nan,1,4,3]
        }
#newIndex = ["A","B","C","D","E","F","G"]
newIndex = ["A","B","C","D","E","F"]

df = pd.DataFrame(data,index = newIndex)

print(df)

#val = #...
#print("Getting value:",df._get_value("A","Part 2"))

for index,series in df.iterrows():
    if int (series["Part 1"]) == int(1):
        df.drop(index,axis = 0, inplace = True)
#    print(series["Part 2"])


#print("Checking if there are any NaN values\n", df.isnull())
#print(df.notnull())

#print(df.dropna(0,'any'))
#print(df.dropna(0,'all))
#print(df.dropna(1, thresh = 5))

#print(df.drop_duplicates()) #row E and part 4 have been dropped because they are duplicates
#print(df.drop_duplicates(subset = ["Part 1", "Part 4"], keep = "first")) 
print(df.drop_duplicates(subset = ["Part 1", "Part 4"], keep = "last", inplace = False)) 
#print(df.drop_duplicates(subset = ["Nan Part", "Part 4"],keep = False)) 

#df = df.drop("A","C","D",axis = 0)
#print(df)
