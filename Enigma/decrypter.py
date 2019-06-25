#Author: Zach Page
#Date: 6/18/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: decrypter.py
#Desc: Provides inverted dictionary of plugboard
import plugboard
defaultDict = plugboard.getPlugboard()
def invertedDict(invert = defaultDict): #returns the inverted version of the plugboard
    inv_dict = {v: k for k, v in invert.items()}
    return inv_dict
