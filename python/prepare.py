import pandas as pd
import numpy as np
import math
import pickle
from sklearn.model_selection import train_test_split



df = pd.read_csv("C:/Files/ML-Dataset/enter the travel verse/python/newData.csv")
df.rename(columns={
    "'ISSUE_DATE'" : "TICKET_DATE",
    "'DEPARTURE_DATE'":"FLIGHT_DATE",
    "'TRIP_TYPE'" : "TRIP_TYPE",
    "'CABIN'" : "CABIN",
    "'ORIGIN'" : "START",
    "'DESTINATION'" : "END",
    }, inplace=True)

df = df[['TICKET_DATE','FLIGHT_DATE','TRIP_TYPE','CABIN','START','END']]
for i, col in enumerate(df.columns):
    df.iloc[:, i] = df.iloc[:, i].str.replace("'", '')

df['FLIGHT_DATE'] = pd.to_datetime(df['FLIGHT_DATE'])
df['TICKET_DATE'] = pd.to_datetime(df['TICKET_DATE'])

df['DURATION'] = df['FLIGHT_DATE'] - df['TICKET_DATE']
df['DURATION'] = df['DURATION'] / np.timedelta64(1, 'D')

print(df[df['DURATION'] < 0])

# gps = pd.read_csv("C:/Files/ML-Dataset/enter the travel verse/dataset/airport-codes_csv.csv")
# gps = gps[['iata_code','coordinates']]
# gps.dropna(inplace=True)
# gps.set_index("iata_code", inplace = True)

# for index, i in enumerate(df.index):
#     print(index, end="\r")
#     try:
#         df.at[i, "START"] = gps.at[df.at[i, "START"], "coordinates"]
#         df.at[i, "END"] = gps.at[df.at[i, "END"], "coordinates"]
#     except:
#         continue


# for index, i in enumerate(df.index):
#     print(index, end="\r")
#     try:
#         df.at[i, "START"] = df.at[i, "START"].split(',')
#         df.at[i, "END"] = df.at[i, "END"].split(',')

#         df.at[i, "START_LAT"] = "{:.3f}".format(float(df.at[i, "START"][0]))
        
#         df.at[i, "START_LONG"] = "{:.3f}".format(float(df.at[i, "START"][1]))
        

#         df.at[i, "END_LAT"] =  "{:.3f}".format(float(df.at[i, "END"][0]))
#         df.at[i, "END_LONG"] = "{:.3f}".format(float(df.at[i, "END"][1]))
#     except:
#         continue



# df.drop(["START", "END"], axis=1, inplace=True)
# df.dropna(inplace=True)

# print(df.head())

# df.to_csv('trainData.csv', index=False)
#----------------------------------------------------------------------------

# df.rename(columns={
#     "'ISSUE_DATE'" : "TICKET_DATE",
#     "'DEPARTURE_DATE'":"FLIGHT_DATE",
#     "'TRIP_TYPE'" : "TRIP_TYPE",
#     "'CABIN'" : "CABIN",
#     "'ORIGIN'" : "START",
#     "'DESTINATION'" : "END",
#     }, inplace=True)

# df = df[['TICKET_DATE','FLIGHT_DATE','TRIP_TYPE','CABIN','START','END']]
# for i, col in enumerate(df.columns):
#     df.iloc[:, i] = df.iloc[:, i].str.replace("'", '')

# df['FLIGHT_DATE'] = pd.to_datetime(df['FLIGHT_DATE'])
# df['TICKET_DATE'] = pd.to_datetime(df['TICKET_DATE'])

# df['DURATION'] = df['FLIGHT_DATE'] - df['TICKET_DATE']
# df['DURATION'] = df['DURATION'] / np.timedelta64(1, 'D')

# df['MONTH'] = df['FLIGHT_DATE'].dt.month
# df['DAY'] = df['FLIGHT_DATE'].dt.dayofweek
# df['WEEK'] = pd.to_numeric(df['FLIGHT_DATE'].dt.day/7)
# df['WEEK'] = df['WEEK'].apply(lambda x: math.ceil(x))

# df['TRIP_TYPE'].loc[(df['TRIP_TYPE'] == 'OW')] = 0
# df['TRIP_TYPE'].loc[(df['TRIP_TYPE'] == 'RT')] = 1
# df['TRIP_TYPE'].loc[(df['TRIP_TYPE'] == 'XX')] = 2

# df['CABIN'].loc[(df['CABIN'] == 'Econ')] = 0
# df['CABIN'].loc[(df['CABIN'] == 'Prem')] = 1

# df = df[['MONTH','DAY','WEEK' ,'DURATION','TRIP_TYPE','CABIN','START','END']]

# print(df.head())

# df.to_csv('data_final.csv', index=False)














# ----------------------------------------------------------------------------------------------------------------------
# f = open("C:/Files/ML-Dataset/enter the travel verse/python/newData.csv", "r")
# Lines = f.readlines()
# indexCount = []
# for i in range(len(Lines)):
#     if Lines[i].strip().count(',') != 15:
#         indexCount.append(i)
# print(len(Lines))
# print(len(indexCount))


# print('poping')
# new_list = sorted(indexCount, reverse=True)

# for i, index in enumerate(new_list):
#     print(i, end='\r')
#     del Lines[index]

# print(len(Lines))
# print('done')

# with open('newData2.csv', 'w') as f:
#     for item in Lines:
#         f.write("%s\n" % item)

# print("Done")

# 'SEG_NUMBER','MARKETING_AIRLINE','MARKETING_AIRLINE_CD','FLIGHT_NUMBER','CABIN','ORIGIN','DESTINATION','DEPARTURE_DATE'

# df.rename(columns={
#     "'ISSUE_DATE'" : "TICKET_DATE",
#     "'DEPARTURE_DATE'":"FLIGHT_DATE",
#     "'TRIP_TYPE'" : "TRIP_TYPE",
#     "'CABIN'" : "CABIN",
#     "'ORIGIN'" : "START",
#     "'DESTINATION'" : "END",
#     }, inplace=True)

# df = df[['TICKET_DATE','FLIGHT_DATE','TRIP_TYPE','CABIN','START','END']]
# for i, col in enumerate(df.columns):
#     df.iloc[:, i] = df.iloc[:, i].str.replace("'", '')

# details = {
#     'Name' : ["'Ankit'", "'Aishwarya'", "'Shaurya'", "'Shivangi'"],
#     'FLIGHT_DATE' : ["'2018-08-03'", "'2018-08-12'", "'2018-08-15'", "'\\N'"],
# }

# df = pd.DataFrame(details)

# for i, col in enumerate(df.columns):
#     df.iloc[:, i] = df.iloc[:, i].str.replace("'", '')