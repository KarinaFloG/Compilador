#Para manejo de archivos xlsx
import pandas as pd
#Para manejo de expresiones regulares
import re
#Para manejo de saltos de linea 
import os

#Para leer el archivo csv que contiene los mnemonicos
xls = pd.ExcelFile('68HC11.xlsx')
#Para imprimir el nombre de las hojas de excel(Una hoja por mnemonico)
print(xls.sheet_names)
#Para convertir a data frame todos los mnemonicos(Cada hoja)
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

#print(df.head())
#print(df['OPCODE'])
#for row in sheet.iter_rows():
#	print(row[0].value)

#Para abrir el archivo que contiene el código a compilar
try:
 	file = open("pro.asc","r")
 	print("Se pudo abrir el archivo")
except:
 	file = "Error"
 	print("Error al abrir el archivo")
#Imprime el archivo que abrimos
#print(f.read())

#Variable para contar los comentarios
coment = 0
#Para leer el archivo linea por linea
#for linea in file:
#	linea2 = linea[:-1]
	#Para reconocer los comentarios
#	if linea[0] == '*':
#		coment = coment + 1
#print("Comentarios:" + str(coment))

#Para compilar la expresión regular que busca los EQU	
patronEQU = re.compile(r'\w+(\s)+(EQU)(\s)+\$\d+')
#Para compilar la expresión regular que busca los ORG	
patronORG = re.compile(r'(\s)+(ORG)(\s)+\$\d+')
#Para compilar la expresión regular que busvca los FCB	
patronFCB = re.compile(r'(\s)+(FCB|fcb)(\s)+\$\w+\d+,\$\w+\d+')
#Para compilar la expresión regular que busvca los END	
patronEND = re.compile(r'(\s)+(END|end|End)(\s)+\$\d+')
#Para compilar la expresión regular que busca los comentarios	
patronCOMMENT = re.compile(r'(\*(\s+\w+)+\s\-(\w+\s)+\w+\-)|(\*(\s+\w+)+\s+\w+\-\w+)|(\*(\s+\w+)+\s+\(\w+((\s+\w+)+)*\))|(\*(\w+\s)+)(\*\s(\w+\s)+)|((\*\s(\w+\s{1,3})+))|(\*\s(\w+\s)+)|(\*(\ \s{1,5})(\w+\s)+)|(\*(\w+\s)+)|(\*+)')

numEQU = 0
numORG = 0
numFCB = 0
numEND = 0
numCOMMENT = 0
numLineas = 0
with open("pro.asc","r") as f:
	list_lines = f.readlines()
	for line in list_lines:
		numLineas = numLineas + 1
		#Para buscar coincidencias de los EQU
		if re.search(patronEQU,line):
			print(line)
			numEQU = numEQU +1
			print(numEQU)
		#Para buscar coincidencias de los ORG
		if re.search(patronORG,line):
			numORG = numORG + 1
			print("Numero de org: ")
			print(numORG)
		#Para buscar coincidencias de los FCB
		if re.search(patronFCB,line):
			numFCB = numFCB + 1
			print("Numero de FCB: ")
			print(numFCB)
		#Para buscar coincidencias de los END
		if re.search(patronEND, line):
			numEND = numEND + 1
			print("Numero de END: ")
			print(numEND)

		if re.search(patronCOMMENT,line):
			numCOMMENT = numCOMMENT + 1
			print("Num de comentarios: ")
			print(numCOMMENT)
fileMotorola = open("motorola.lst","w")
print("Rango")
print(range(numLineas))
for i in range(numLineas):
	fileMotorola.write(str(i) +" A")

fileMotorola.close()