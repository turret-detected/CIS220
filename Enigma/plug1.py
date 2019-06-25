#Author: Patrick Devine
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: plug1.py
#Desc: Initial encryption functionality

import plugboard
plug = plugboard.getPlugboard()
plug.update({" ":" ","\n":"\n"}) #temporary until character validation is added
   
def translate(phrase,dictionary=plug): #each string char is a key from dict, outputs value
    translation = ""
    for letter in phrase:
        #print (letter, 'corresponds to', plug[letter])
        translation += dictionary[letter]
    return translation

#TODO	
#add to for loop
#
#if char is in dict keys
#	translate char, add to string
#else
#	if char is a space
#		count++
#		add space to string
#	if char is a newline
#		pass
#	else
#		add char to string
#
#if count >= 5
#	count = 0
#	add newline to string
