#Author: Patrick Devine
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: plug1.py
#Desc: Initial encryption functionality

import plugboard
plug = plugboard.getPlugboard()
#plug.update({" ":" ","\n":"\n"}) #temporary until character validation is added
   
def translate(phrase,dictionary=plug): #each string char is a key from dict, outputs value
	count = 0
	translation = ""
	for char in phrase:
		if count == 5:
			count = 0
			#print("adding newline") #DEBUG
			translation += "\n" 
		
		if char in dictionary.values():
			translation += dictionary[char]	  
		else:
			if char == " ":
				count = count + 1
				#print("Adding count" + str(count)) #DEBUG
				translation	 += " "
			elif char ==  "\n":
				pass
			else:
				translation += char 
		
	#print(translation)	#DEBUG	
	return translation

