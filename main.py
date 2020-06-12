import numpy as np
import pandas as pd
import openpyxl
import xlsxwriter
# import tensorflow as tf

# Currently this file will read in the excel doc into a dictionary of dataframes.
# The name of the worksheet becomes the dictionary key and the worksheet itself becomes the dataframe.
# The column names are currently: 'FRONT OFFICE / PBX/ GUEST SERVICES SCHEDULE', 'Unnamed: 1' - 'Unnamed: 10'
# The below script simply removed the employee names and replaced them with EMPLOYEE for privacy reasons.
# Note there are some worksheets with 16000 empty columns and I want to remove those somehow.
# Note that 'Front Office Schedule 2.0_For_ML.xlsx' is very large, you may want to work on 'mini FO Test.xlsx' to test methods of working
# with the data and then switch to the larger file once you know it works on the final three dataframes
dfs = pd.read_excel('Front Office Schedule 2.0_For_ML.xlsx', sheet_name=None)
# print(dfs)
# print(dfs.keys())
# print(dfs['12.16'].values())
# print(dfs['12.16'].keys())
# print(dfs['12.16']['FRONT OFFICE / PBX/ GUEST SERVICES SCHEDULE']
#       .apply(lambda x: 'Employee' if(x not in noTouch) else x))
noTouch = ['Day:', 'Date:', 'Occ. %:', 'Arrivals:', 'Departures:', 'FRONT OFFICE / PBX/ GUEST SERVICES SCHEDULE', 'MANAGERS',
           'ROOMS CONTROL', 'GUEST EXPERIENCE COORDINATOR', 'NIGHT AUDIT', 'HOSTS', 'PBX', 'Reg.Occ', 'BELLMAN', 'Planned', 'Scheduled', 'Front Office']
# Here we are looping through the dictionary keys and working on the dataframes cooresponding to them. We only needed to anonymize the first column.
for i in dfs.keys():
    dfs[i]['FRONT OFFICE / PBX/ GUEST SERVICES SCHEDULE'] = dfs[i]['FRONT OFFICE / PBX/ GUEST SERVICES SCHEDULE'].apply(
        lambda x: 'Employee' if(x not in noTouch) else x)
    if('Unnamed: 9' in dfs[i].columns):
        dfs[i] = dfs[i].drop(['Unnamed: 9'], axis=1)
# This will show how the data looks in memory
# print(dfs)

# This will write all the dataframes back into excel worksheets
# writer = pd.ExcelWriter('new.xlsx', engine='xlsxwriter')
# for sheet_name in dfs.keys():
#     dfs[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

# writer.save()
