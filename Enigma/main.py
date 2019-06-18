#Author: Andrew Mohnkern
#Date: 6/9/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: main.py
#Desc: Primary Enigma class


import menu
import fileprovider
import plugboard

returntomain = True
userin = ""


while returntomain == True:
	returntomain = False
	menu.welcome_menu()
	userin = input()
	
	if userin == "I":
		menu.instruction_menu()
		null = input()
		returntomain = True
		
	elif userin == "E":
		fileToEncrypt = fileprovider.getTextFilePath()
		
		
	elif userin == "D":
		print("NYI")
		returntomain = True
		
	#elif userin == "K":
	#	keyFile = fileprovider.getKeyFilePath()
	#	print(keyFile)
	#	print(fileprovider.convertCSVToDict(keyFile))
		
	elif userin == "Q":
		print("Goodbye")
		
	else:
		print("Invalid Command")
		returntomain = True

