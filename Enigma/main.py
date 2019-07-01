#Author: Andrew Mohnkern
#Date: 6/9/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: main.py
#Desc: Primary Enigma class

import menu
import utilities
import plugboard
import plug1

returntomain = True
userin = ""


while returntomain == True:
	returntomain = False
	menu.welcome_menu()
	userin = input("> ")
			
	if userin == "E": #File selection, encrypts, outputs to another file
		utilities.encryptText()

		print("Press any key to return to main menu")
		test = input()
		print("Returning the main menu")
		returntomain = True
		
	elif userin == "D": #File selection, decrypts, outputs to another file
		utilities.decryptText()
		
		print("Press any key to return to main menu")
		test = input()
		print("Returning the main menu")
		returntomain = True
		
	elif userin == "Q":
		print("Goodbye")
		
	else:
		print("Invalid Command")
		returntomain = True

