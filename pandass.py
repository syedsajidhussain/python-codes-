# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:30:33 2024

@author: syed.hussain
"""

import pandas as pd
import numpy as np

np.arange(0,20).reshape(5,4)

df=pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1", "Row2",
                                    "Row3", "Row4",
                                          "Row5"  ], columns=["column1","column2",
                                                              "column3", "column4"])
                                                              
df.head()


df.tail()
df.describe()



##using row index name loc
df.loc[['Row3','Row4']]



df.iloc[2:4,0:2]

df.iloc[2:,1:]

##convert dataframe into arrays
df.iloc[:,1:].values


df=pd.DataFrame(data=[[1,np.nan,2],[1,3,4]],index=["Row1",
                                                      "Row2"],columns=["Column1",
                                                                             "Column2",
                                                                             "Column3",
                                                                             ])
df                                                                       
