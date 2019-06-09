#BASIC SCRPT TO CREATE DATE FEATURES

import pandas as pd
import numpy as np

df = pd.read_csv("day.csv")

df['dteday'] = pd.to_datetime(df['dteday'])

#weekday
df ["weekday"] = df['dteday'].dt.weekday

#workingday
for i,row in df.iterrows():
    if (row.weekday==5) | (row.weekday==6):
        df.at[i,"workingday"]=0
    else :
        df.at[i,"workingday"]=1
#month        
df ["mnth"] = df['dteday'].dt.month

#year
df ["yr"] = df['dteday'].dt.year
for i,row in df.iterrows():
    if row.yr==2011:
        df.at[i,"yr"]=0
    else :
        df.at[i,"yr"]=1
            
#season
season_month=[1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
for i,row in df.iterrows():
    df.at[i,"season"]=season_month[row.mnth-1]
    
#holiday
from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays(start='2011-01-01', end='2012-12-31').to_pydatetime()

for i,row in df.iterrows():
    if row.dteday in holidays:
        df.at[i,"holiday"]=1
    else:
        df.at[i,"holiday"]=0
            
df.to_csv('day.csv', index=False)