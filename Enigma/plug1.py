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
