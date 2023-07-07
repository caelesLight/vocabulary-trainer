import random
import os
import time
import msvcrt
import select
import sys
import threading

dic = {
'la inundación': 'Überschwemmung',
'el calentamiento': 'Erwärmung',
'derretir': 'Schmelzen',
'el suelo seco': 'Trockener Boden',
'frecuente': 'häufig',
'el efecto invernadero': 'Treibhauseffekt',
'la primavera': 'Der Frühling',
'afectar': 'Beeinflussen',
'potable': 'Trinkbar',
'el calor': 'Wärme',
'glaciares': 'Gletscher',
'el cambio climático': 'Klimawandel',
'energía solar': 'Solar Anergie',
'dióxido de carbono': 'Kohlenstoffdioxid',
'emisiones': 'Emissionen',
'apagar': 'Ausschalten',
'ahorrar agua': 'Wassersparen',
'reciclar basura': 'Recycling von Müll',
'utilizar': 'Verwenden',
'las energías renovables': 'Erneuerbare Energien',
'panel fotovoltaico': 'Fotovoltaik-Panel',
'el colector solar': 'Solarkollektor',
'espacio': 'Raum',
'la escasez de agua': 'Wasserknappheit',
'el oso polar': 'Eisbär',
'la temperatura de tierra sube': 'Die Temperatur der Erde steigt.',
'breve': 'kurz',
'la ventaja': 'Vorteile',
'la desventaja': 'Nachteil',
'por lo tanto': 'daher',
'a pasar de': 'trotz',
'sin embargo': 'jedoch',
'además': 'außerdem',
'entretanto': 'in der Zwischenzeit',
'el abuso': 'Missbrauch',
'el abandono': 'Aussetzung',
'la pobreza': 'Armut',
'la prostitución': 'Prostitution',
'la humillación': 'Demütigung',
'el asesinato': 'Mord',
'sobrevivir': 'Überleben',
'pidiendo limosna': 'Betteln',
'vender': 'Verkaufen',
'el chicle': 'Kaugummi',
'monarquía parlamentaria': 'parlamentarische Monarchie',
'función presentativa': 'Präsentative Funktion',
'corona': 'Krone',
'hereditaria': 'Vererblich',
'disolver': 'auflösen',
'el jefe de gobierno': 'Regierungschef',
'el jefe de estado': 'das Staatsoberhaupt',
'proponer': 'Vorschlagen',
'los ministros': 'Minister',
'el canciller': 'Kanzler',
'ejecutivo': 'Exekutive',
'judicativo': 'Judikative',
'legislativo': 'Legislative',
'elegir, votar': 'wählen',
'el embalaje': 'Verpackung',
"el tribunal": "Das Gericht",
"el tribunal supremo": "Das höchste Gericht",
"consiste en": "besteht aus",
"miembros": "Mitglieder",
"Los Cortes Generales": "Generalkommissionen",
"el congreso": "Der Kongress",
"el senado": "Der Senat",
"la subalimentación": "Unterernährung",
"de las Fuerzas Armadas": "die Streitkräfte",
"mostrar": "zeigen",
"en la parte de arriba": "oben",
"en la parte de abajo": "unten",
"en el primer plano": "im Vordergrund",
"en el segundo plano": "weiter hinten",
"al fondo": "im Hintergrund",
"a la izquierda": "links",
"a la derecha": "rechts",
"en el centro": "in der Mitte",
"en el borde": "am Rand",
"al lado de": "neben",
"delante de": "vor",
"enfrente de": "vor/gegenüber von",
"detrás de": "hinter",
"debajo de": "unter",
"encima de": "über",
"el ambiente": "die Stimmung",
"según": "bezüglich",
"referirse a": "Sich beziehen auf",
"la imagen llama atención sobre": "Das Bild lenkt die Aufmerksamkeit auf",
"el punto focal": "Der Schwerpunkt",
"a primera vista": "Auf dem ersten Blick",
"nivel de vida": "Lebensstandard",
"Desarrollo": "Entwicklung",
"Detener": "Stoppen"
}

dicV = list(dic.values())

clear = lambda: os.system('cls')
colorN = lambda: os.system('color 7')
colorG = lambda: os.system('color A')
colorR = lambda: os.system('color C')

colorN()
clear()

rDic = {value: key for key, value in dic.items()}
progRep = True
missT = False

while progRep:

	err = 0
	finished = False
	sDicV = random.sample(dicV, len(dicV))

	clear()
	print("Welcome to Vocabulary Trainer!")
	print('You can leave everytime with "exit()"')
	print("Type any key to start the lesson!")

	inpS = input("Start: ")

	clear()


	while len(sDicV) >= 1:
		colorN()
		print(f'{sDicV[0]}    ({len(dicV)-len(sDicV)}/{len(dicV)})')
		imp = input()
	
		if imp == rDic[sDicV[0]] or imp == rDic[sDicV[0]] + " ":
			
			colorG()

			if missT == False:
				del sDicV[0]
			missT = False
			random.shuffle(sDicV)
			time.sleep(0.5)
			colorN()
			clear()
	
		elif imp == "exit()":
			break

		else:
			colorR()
			print(f'false correct: {rDic[sDicV[0]]}')
			err = err + 1
			missT = True

			key = msvcrt.getch()
			if key == b'\r':
				print("")

			colorN()
			clear()
	
		if len(sDicV) < 1:
			finished = True

	if finished:
		print("You finished your learning session!")
		print(f'Errors: {err}')
	else:
		print("you already leaving?")

	print("Do you want to Start a new session (y/n)")
	resp = input()
	if resp == 'n':
		progRep = False


	

