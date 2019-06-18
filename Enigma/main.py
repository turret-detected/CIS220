#Author: Andrew Mohnkern
#Date: 6/9/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: main.py
#Desc: Primary Enigma class


import menu
import fileprovider
import plugboard
import plug1

returntomain = True
userin = ""


while returntomain == True:
	returntomain = False
	menu.welcome_menu()
	userin = input()
	
	#if userin == "I":
	#	menu.instruction_menu()
	#	null = input()
	#	returntomain = True
		
	if userin == "E":
		fileToEncrypt = fileprovider.getTextFilePath()
		fileText = fileprovider.convertFileToText(fileToEncrypt)
		fixedText = fileprovider.fixText(fileText)
		
		newText = plug1.translate(fixedText)
		print("Output: \n")
		print(newText)
		print("\n")
		
		print("Returning the main menu")
		returntomain = True
		
		
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

