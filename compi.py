import pandas as pd #Para manejo de archivos xlsx
import re #Para manejo de expresiones regulares
import os #Para manejo de saltos de linea 
#---------------Variables globales
lista_variables = [] #Lista para almacenar variables (EQU)
lista_org = [] #Lista para almancenar los org
lista_end = [] #Lista para almacenar los end
lista_fcb = [] #Lista para almacenar los fcb
#----------------Expresiones regulares
patronEQU = re.compile(r'\w+(\s)+(equ|Equ|EQU)(\s)+\$\d+') #Para compilar la ER que busca los EQU	
patronORG = re.compile(r'(\s)+(org|Org|ORG)(\s)+\$\w+') #Para compilar la ER que busca los ORG	
patronFCB = re.compile(r'(\s)+(fcb|Fcb|FCB)(\s)+\$\w+\d+,\$\w+\d+')#Para compilar la ER que busvca los FCB
patronEND = re.compile(r'(\s)+(end|End|END)(\s)+\$\d+')#Para compilar la ER que busvca los END	
patronCOMMENT = re.compile(r'\*[^\n]*(\n)')#Para compilar la ER que busca comentarios
#-------------Lista con tipos de errores
lista_errores = [["001","CONSTANTE INEXISTENTE"],["002","VARIABLE INEXISTENTE"],["003","ETIQUETA INEXISTENTE"],["004","MNEMÓNICO INEXISTENTE"],
["005","INSTRUCCIÓN CARECE DE OPERANDO(S)"],["006","INSTRUCCIÓN NO LLEVA OPERANDO(S)"],["007","MAGNITUD DE OPERANDO ERRONEA"],
["008","SALTO RELATIVO MUY LEJANO"],["009","INSTRUCCIÓN CARECE DE AL MENOS UN ESPACIO RELATIVO AL MARGEN"],["010","NO SE ENCUENTRA END"]]
try:
 	file2 = open("pro2.asc","w")#Para abrir el archivo que no tendra comentarios
 	#print("Se pudo crear el archivo sin comentarios")
except:
 	file2 = "Error"
 	#print("Error al crear el archivo sin comentarios")

#-----------------Función para eliminar comentarios del archivo (Primera pasada)------------
def archivo_sinComentarios():
	numCOMMENT= 0 #Contador
	with open("pro.asc","r") as f:#Con el archivo abierto
		list_lines = f.readlines() #Lee el numero de lineas
		for line in list_lines: #Recorre el arcjhivo
			if re.search(patronCOMMENT,line): #Busca coincidencias con la expresion regular
				numCOMMENT = numCOMMENT + 1 #Si hay coincidencia aumenta el contador
				x = line.split('*') #Con lo que reconoce los comentarios después de lineas con texto
				file2.write(x[0]+"\n") #Escribe sobre el archivo sin comentarios
				#print(x[0])
			else:
				file2.write(line) #Escribe todo lo que no tiene comentarios
	print("Primera pasada con éxito")

#-------------Función para reconocer directivas de ensamblador
def search_directivas():
	#Contadores
	numEQU = 0
	numORG = 0
	numFCB = 0
	numEND = 0
	numCOMMENT = 0
	numLineas = 0
	ultimoEQU = 0
	ulimoORG = 0
	ultimoEND = 0
	ultimoFCB = 0
	lista_prov = []
	tamanio = 0
	separador = " " #Separador para dividir las cadenas del EQU

	with open("pro2.asc","r") as f:
		list_lines = f.readlines() #Para leer todas las lineas del archivo
		for line in list_lines:
			numLineas = numLineas + 1
			#Para buscar coincidencias de los EQU
			if re.search(patronEQU,line): #Para buscar EQU con la expresión regular
				cadena_separada = line.split(separador) #Si una cadena cumple con la expresión, la separa y guarda en una lista
				ultimoEQU= len(cadena_separada)#Para saber la cantidad de elementos en que se separo la cadena 
				lista_variables.append([cadena_separada[0],cadena_separada[ultimoEQU-1]]) #Agrega el nombre y el valor de las variables a una lista


			#Para buscar coincidencias con los END
			if re.search(patronEND,line):
				numEND = numEND + 1#Contador para el numero de end
				#print(numEND)
				line = line.lstrip() #Elimina todos los espacios que tiene al principio un end
				lista_prov.append(line) #Agrega la cadena sin espacios a una lista
				for i in lista_prov:#Recorre la lista anterios
					cadena_separada = line.split(separador)#Separa la cadena, cambia espacios por comas
					ultimoEND = len(cadena_separada)#Obtiene el tamaño de la cadena anterior
					lista_end.append([cadena_separada[0],cadena_separada[ultimoEND-1]])#Agrega a la lista final los end y las direcciones
				
			if re.search(patronFCB,line):
				line = line.lstrip("RESET")
				line = line.lstrip()
				lista_prov.append(line)
				#print(lista_prov)
				tamanio = len(lista_prov)
				for i in lista_prov:
					i = i.rsplit()
					lista_fcb.append(i)

			#Para buscar coincidencias de los ORG
			if re.search(patronORG,line):
				numORG = numORG +1 #contador para el numero de org
				#print("NUM OR:",+ numORG) 
				#print(line)
				line = line.rsplit() #quita espacios de los org y guarda en un vector
				lista_org.append(line)#guarda en una lista los vectores






#------Principal-------
archivo_sinComentarios()
file2.close()
search_directivas()
print(lista_fcb)




	
					




