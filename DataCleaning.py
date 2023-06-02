import pandas as pd 

dataco2 = pd.read_excel("./CO2 emissions defined period.xlsx", sheet_name="Cleaned data")

print(dataco2.isnull().count())
#print(dataco2.isnull().values.any())

print((dataco2.loc[dataco2['Country code'] == "DEU"]) and (dataco2.loc(dataco2['Year'] == 2020)))
print("----------")