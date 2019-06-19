# -*- unicode: utf-8 -*-

'''
Ler coordenadas do arquivo excel
'''
# Biblioteca importada para ler arquivos excel!
import xlrd

la2203 = [] # informacoes do aviao la2203
gz0331 = [] # informacoes do aviao gz0331
az0032 = [] # informacoes do aviao az0032
az0157 = [] # informacoes do aviao az0157
gz0667 = [] # informacoes do aviao gz0667


#def ler_planilha(planilhaDeRadar):

book = xlrd.open_workbook("planilhaDeRadar.xlsx")
sh = book.sheet_by_index(0) # Ler informacoes da primeira planilha
print("Lendo planilha...\n\n")


for rx in range(sh.nrows): # para cada linha(rx) no range do numero de linhas da planilha

	# Se o valor na linha rx na terceita coluna for igual a 'LA 2203' entao adicionar todos valores na lista la2203!
	if sh.row_values(rx,0,8)[2] == 'LA 2203':
		la2203.append(sh.row_values(rx,0,8))

	# Se o valor na linha rx na terceita coluna for igual a 'GZ 0331' entao adicionar todos valores na lista gz0331!
	if sh.row_values(rx,0,8)[2] == 'GZ 0331':
		gz0331.append(sh.row_values(rx,0,8))

	# Se o valor na linha rx na terceita coluna for igual a 'AZ 0032' entao adicionar todos valores na lista az0032!
	if sh.row_values(rx,0,8)[2] == 'AZ 0032':
		az0032.append(sh.row_values(rx,0,8))

	# Se o valor na linha rx na terceita coluna for igual a 'AZ 0157' entao adicionar todos valores na lista az0157!
	if sh.row_values(rx,0,8)[2] == 'AZ 0157':
		az0157.append(sh.row_values(rx,0,8))

	# Se o valor na linha rx na terceita coluna for igual a 'GZ 0667' entao adicionar todos valores na lista gz0667!
	if sh.row_values(rx,0,8)[2] == 'GZ 0667':
		gz0667.append(sh.row_values(rx,0,8))	


	'''
	print("::::::::::::::::::::::::::::::::")

	for num in la2203:
		print(num)

	print("::::::::::::::::::::::::::::::::")

	for num in gz0331:
		print(num)

	print("::::::::::::::::::::::::::::::::")

	for num in az0032:
		print(num)

	print("::::::::::::::::::::::::::::::::")
	
	for num in az0157:
		print(num)

	print("::::::::::::::::::::::::::::::::")

	for num in gz0667:
		print(num)

	print("::::::::::::::::::::::::::::::::")

	'''

def getLA2203():
	return la2203

def getGZ0331():
	return gz0331

def getAZ0032():
	return az0032

def getAZ0157():
	return az0157

def getGZ0667():
	return gz0667

'''
def testeget():
	a = getLA2203()
	b = getGZ0331()
	c = getAZ0032()
	d = getAZ0157()
	e = getGZ0667()

	for x in a:
		print(x)
	print("::::::::::::::::::::::::::::::::")
	for x in b:
		print(x)
	print("::::::::::::::::::::::::::::::::")
	for x in c:
		print(x)
	print("::::::::::::::::::::::::::::::::")
	for x in d:
		print(x)
	print("::::::::::::::::::::::::::::::::")
	for x in e:
		print(x)
	print("::::::::::::::::::::::::::::::::")

#ler_planilha('planilhaDeRadar.xlsx')
testeget()
'''