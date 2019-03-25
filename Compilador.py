import pandas as pd
#Para leer un archivo csv
xls = pd.ExcelFile('68HC11.xlsx')
#Para imprimir el nombre de las hojas de excel
print(xls.sheet_names)
#Para convertir a data frame
df = xls.parse('Inmediato')
df2 = xls.parse('Directo')
df3 = xls.parse('IndX')
df4 = xls.parse('IndY')
df5 = xls.parse('Inherente')
df6 = xls.parse('Extendido')
df7 = xls.parse('Relativo')
df8 = xls.parse('BEstados')
#Para imprimir el dataframe
#print(df)

print(df.head())
print(df['OPCODE'])
#for row in sheet.iter_rows():
#	print(row[0].value)
