#Author: Zach Page
#Date: 6/18/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: decrypter.py
#Desc: Provides inverted dictionary of plugboard

def invertedDict(): #returns the inverted version of the plugboard
    import plugboard
    invert = plugboard.getPlugboard()
    inv_dict = {v: k for k, v in invert.items()}
    return inv_dict

#TODO
#The function should take a dictionary as an argument
#However it's default should be the plugboard dictionary
