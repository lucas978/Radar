# -*- unicode: utf-8 -*-

'''
Ler coordenadas do arquivo excel
'''
# Biblioteca importada para ler arquivos excel!
import xlrd

'''
# Metodo para ler arquivo .xls
def xlread(arquivo_xls):
'''
	#Gerador que le arquivo .xls
'''

	# Abre o arquivo
	xls = xlrd.open_workbook("planilhaDeRadar.xlsx")
	# Se o nome do arquivo estiver como xls, alterar o valor passado como parametro
	# de xlsx -> xls, isso vale para todos os metodos que utilizam o nome do arquivo


	# Pega a primeira planilha do arquivo
	plan = xls.sheets()[0]

	# Para i de zero ao numero de linhas da planilha
	for i in range(plan.nrows):
		# Le os valores nas linhas geradas da planilha
		yield plan.row_values(i)



def xlprint(arquivo_xls):
	for line in xlread(arquivo_xls):
		print(line)
'''

'''
FUNCIONANDO -- PEGANDO O PRIMEIRO TEMPO DOS VOOS

def estado_inicial(planilhaDeRadar):
	col_temporizador = []
	col_status = []
	col_voo = []
	col_dist = []
	col_vel = []
	col_x = []
	col_y = []
	col_z = []

	book = xlrd.open_workbook("planilhaDeRadar.xlsx")
	sh = book.sheet_by_index(0)
	for rx in range(sh.ncols - 1):
	    #print(sh.row(rx))
	    #if sh.row(rx)[0]
		if sh.row(rx)[0]: 
		    #print(sh.row(rx)[0])
		    col_temporizador.append(str(sh.cell_value(rx, 0)))

		if sh.row(rx)[0]:
			col_status.append(str(sh.cell_value(rx , 1)))

		if sh.row(rx)[0]:
			col_voo.append(str(sh.cell_value(rx , 2)))

		if sh.row(rx)[0]:
			col_dist.append(str(sh.cell_value(rx , 3)))

		if sh.row(rx)[0]:
			col_vel.append(str(sh.cell_value(rx , 4)))

		if sh.row(rx)[0]:
			col_x.append(str(sh.cell_value(rx , 5)))

		if sh.row(rx)[0]:
			col_y.append(str(sh.cell_value(rx , 6)))

		if sh.row(rx)[0]:
			col_z.append(str(sh.cell_value(rx , 7)))

	print("Tempo: ",col_temporizador)
	print("Status: ",col_status)
	print("Voo: ", col_voo)
	print("Distancia: ",col_dist)
	print("Velocidade: ",col_vel)
	print("X: ",col_x)
	print("Y: ",col_y)
	print("Z: ",col_z)


'''

def estado_inicial(planilhaDeRadar):
	la2203 = []
	gz0331 = []
	az0032 = []
	az0157 = []
	gz0667 = []

	book = xlrd.open_workbook("planilhaDeRadar.xlsx")
	sh = book.sheet_by_index(0)
	print("Cols:", sh.ncols )
	print("Rows:", sh.nrows)
	
	
	for rx in range(sh.nrows):

		if sh.row_values(rx,0,7)[2] == 'LA 2203':
			la2203.append(sh.row_values(rx,0,7))
		
		if sh.row_values(rx,0,7)[2] == 'GZ 0331':
			gz0331.append(sh.row_values(rx,0,7))
		
		if sh.row_values(rx,0,7)[2] == 'AZ 0032':
			az0032.append(sh.row_values(rx,0,7))
		
		if sh.row_values(rx,0,7)[2] == 'AZ 0157':
			az0157.append(sh.row_values(rx,0,7))
		
		if sh.row_values(rx,0,7)[2] == 'GZ 0667':
			gz0667.append(sh.row_values(rx,0,7))	

	'''
	ct = 0
	for num in la2203:
		#print(ct," - ", num)
		if num[0] == '':
			la2203.remove(num)
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



estado_inicial('planilhaDeRadar.xlsx')

