import pandas as pd

df_csv = pd.read_csv("ventas_enero_csv.csv")

print("DataFrame leído desde CSV:")
print(df_csv)

print("")
df_excel = pd.read_excel("ventas_enero_excel.xlsx")
print("Dataframe leído desde Excel:")
print(df_excel)

print("")
df_excel = pd.read_excel("ventas_enero_excel.xlsx", sheet_name=1)
print("Dataframe leído desde Excel:")
print(df_excel)