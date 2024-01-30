# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:15:23 2024

@author: zical
"""

import pandas

file = pandas.read_csv("country_data.csv")
import pandas as df
print(file)
print(file.info())
import pandas as pd
df = pd.DataFrame(file)
print(df.describe())

import pandas as pd
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())

import pandas as pd
file = pandas.read_csv("diab_data.csv")
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())


import pandas as pd
file = pandas.read_csv("housing_data.csv")
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())

import pandas as pd
file = pandas.read_csv("insurance_data.csv", skiprows=5)
print(file)
print(file.info())
df = pd.DataFrame(file)
print(df.describe())
print(file.describe())




