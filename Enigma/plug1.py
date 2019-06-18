#Author: Patrick Devine
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: plug1.py
#Desc: Initial encryption functionality
import plugboard
plug = plugboard.getPlugboard()
plug.update({" ":" "})
   
def translate(phrase):
    translation = ""
    for letter in phrase:
        #print (letter, 'corresponds to', plug[letter])
        translation += plug[letter]
    return translation
