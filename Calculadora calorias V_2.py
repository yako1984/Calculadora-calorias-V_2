import os.path as path
import sys
import os
import json
import time
from datetime import datetime

datosUsuario = {}

def borrarPantalla(): #Limpia la pantalla en cualquier sistema operativo
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls") 
    
    logoPrincipal()

def logoPrincipal():

	print('''
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗░█████╗░░█████╗░██╗░░░░░  ██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║░░░░░  ██║░░░██║╚════██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░╚═╝███████║██║░░░░░  ╚██╗░██╔╝░░███╔═╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░██╗██╔══██║██║░░░░░  ░╚████╔╝░██╔══╝░░
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝╚█████╔╝██║░░██║███████╗  ░░╚██╔╝░░███████╗
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚══════╝''')

						
	print('\n					                                   by: Yako')
	print('					                                       2021 ')
	


#MENU QUE APARECE AL CARGAR LOS DATOS--------------------------------
def menuDatosCargados():
	borrarPantalla()
	pesoActual = input('\nCual es tu peso actual?: ')
	pesoGuardado = datosUsuario['peso']
	fechaGuardada = datosUsuario['fecha']
	
	borrarPantalla()
	print('\nEstos son tus datos del día '+fechaGuardada+' :\n')
	
	for i,o in datosUsuario.items():
		print(i,':',o)
	
	if pesoActual < pesoGuardado:
		print('\nEnhorabuena has adelgazado!!')
	
	elif pesoActual > pesoGuardado:
		print('\nEstas engordando, hay que ponerse las pilas!!.')
	

#COMPROBAR NOMBRE--------------------------------------------
def comprobarNombre(nombre):
	archivo = ('datos/'+nombre+'_save.json')

	if path.exists(archivo):
		borrarPantalla()
		opcion = input('\nEste nombre ya existe quieres sobreescribirlo o cargar tus datos?.\n[1]Sobreescribir\n[2]Cargar\n[3]salir\n> ')
		
		if opcion == '1':
				print('\nEl último archivo guardado con el nombre "'+nombre+'" se sobreescribira.\n')
			
		elif opcion == '2':
			cargarDatos(nombre)
		
		elif opcion == '3':
			menuPrincipal()		
		
		else:
			print('opción no válida!')
			menuPrincipal()

#-----------GUARDAR DATOS-----------------------------------
def guardarDatos ():
	nombreUsuario = datosUsuario['nombre']
	
	with open('datos/'+nombreUsuario+'_save.json', 'w') as file:
		json.dump(datosUsuario, file, indent=4)
		

#-----------CARGAR DATOS-----------------------------------
def cargarDatos (nombreUsuario):
	
	archivo = ('datos/'+nombreUsuario+'_save.json')

	if path.exists(archivo):
		print('\nTus datos fueron cargardos con éxito :)')
		time.sleep(1)
		
		with open('datos/'+nombreUsuario+'_save.json') as file: #Abre el archivo guardado y lo almacena en archivoGuardado temporalmente
			achivoGuardado = json.load(file)    
		
		for clave, valor in achivoGuardado.items(): #Escribimos los datos leidos en archivoGuardado en el diccionario datosUsuario permanentemente
			datosUsuario[clave] = valor

		menuDatosCargados()
	
	else:
		print('\nNo hay datos guardados con ese nombre, vuelve a intentarlo o haz un cálculo nuevo.')
		time.sleep(4)
		menuPrincipal()

	
	
def actividadFisica (total):
	
	borrarPantalla()
	print('\nCual es tu nivel de actividad fisica?')
	print('\n[1] Sedentario (prácticamente ningún ejerciccio)')
	print('[2] Ligeramente activa/o (ejercicio suaves 1 a 3 veces por semana)')
	print('[3] Moderadamente activa (ejercicio 3 a 5 veces por semana)')
	print('[4] Muy activa (ejercicio 6 a 7 días por semana)')
	print('[5] Persona hiperactiva (ejercicio 2 horas al día, o jornada laboral muy intensa)')
	print('[6] Salir')
	
	opcion = input('> ')

	if opcion == '1':
		totalActividad = total * 1.2
	
	elif opcion == '2':
		totalActividad = total * 1.375

	elif opcion == '3':
		totalActividad = total * 1.55

	elif opcion == '4':
		totalActividad = total * 1.725

	elif opcion == '5':
		totalActividad = total * 1.9
	
	elif opcion == '6':
		exit()

	else:
		print('Escoge una de las 5 opciones, poniendo el numero del 1 al 5.')

	adelgazar = totalActividad-300
	engordar = totalActividad+300
	
	borrarPantalla()
	print('\nEste es tu metabolismo basal:', int(total), 'Kcal.')
	print('\nPara MANTENERTE en tu peso debes consumir:', int(totalActividad), 'Kcal.')
	print('Para ADELGAZAR medio kilo a la semana debes consumir:', int(adelgazar), 'Kcal.')
	print('Para ENGORDAR medio kilo a la semana debes consumir:', int(engordar), 'Kcal.')

	datosUsuario['metabolismoBasal'] = total
	datosUsuario['mantenerPeso'] = totalActividad
	datosUsuario['adelgazar'] = adelgazar
	datosUsuario['engordar'] = engordar

	guardarDatos()

#CALCULO CALORIAS----------------------------------------------------------------------------
def calculoCalorias (opcionUsuario, peso, altura, edad):

	if opcionUsuario == '1':
		totalHombre = (10 * float(peso)) + (6.25 * float(altura)) - (5 * float(edad)) +5
		actividadFisica(totalHombre)
		

	elif opcionUsuario == '2':
		totalMujer = (10 * float(peso)) + (6.25 * float(altura)) - (5 * float(edad)) - 161
		actividadFisica(totalMujer)
	
	elif opcionUsuario == '3':
		print('Adios ha sido un placer tenerte por aqui...')
		time.sleep(2)
		exit()		

	
	else: 
		print('Esta opcion no es valida!\nLas unicas opciones validas son 1 o 2.\n')
		menuPrincipal()

def menuPrincipal ():
	
	borrarPantalla()

	print('\nEscoge una opción: ')
	print('[1]Calcular calorias')
	print('[2]Cargar tu calculo anterior')
	opcion = input('> ')
	
	if opcion == '1':

		borrarPantalla()
		print('\n[1]Hombre: ')
		print('[2]Mujer: ')
		print('[3]Salir')

		opcionGenero = input('> ')
		borrarPantalla()
		nombre = input('\nNombre: ')
		comprobarNombre(nombre) #-------------Comprueba si ya hay datos guardados con el nombre que puso el usuario
		print('\nHola ' +nombre+ '!')
		peso = input('\nEscribe tu peso: ')
		altura = input('Altura (En centimetros): ')
		edad = input('Edad: ')
		fecha = time.strftime("%d/%m/%y")
		
		datosUsuario['fecha'] = fecha
		datosUsuario['nombre'] = nombre
		datosUsuario['peso'] = peso
		datosUsuario['altura'] = altura
		datosUsuario['edad'] = edad

		calculoCalorias(opcionGenero, peso, altura, edad)
	
	elif opcion == '2':
		nombreUsuario = input('\nEscribe tu nombre: ')
		cargarDatos(nombreUsuario)
	
	else:
		print('Opción no válida')
		time.sleep(1)
		menuPrincipal()

while True:
	
	borrarPantalla()
	menuPrincipal()

	input('\nPulsa cualquier tecla para continuar...')
		


#Formula.
#Para hombres: (10 x peso en kg) + (6.25 x altura en cm) – (5 x edad) +5
#Para mujeres: (10 x peso en kg) + (6.25 x altura en cm) – (5 x edad) – 161