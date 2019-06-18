#Author: Andrew Mohnkern, Zach Page
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: fileprovider.py
#Desc: Provides GUI based file selection functions

from tkinter import filedialog
from tkinter import *
import csv


def getKeyFilePath(): #opens GUI file selector for a .csv key file
	keyFile = Tk()
	keyFile.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select key file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	return keyFile.filename
	keyFile.destroy()

def getTextFilePath(): #opens a GUI file selector for a .txt file
	textFile = Tk()
	textFile.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select text file",filetypes = (("text files","*.txt"),("all files","*.*")))
	return textFile.filename
	textFile.destroy()
	
def convertCSVToDict(filepath): #converts a .csv file to a dict
	keyDict = {}
	reader = csv.DictReader(open(filepath, 'r'), delimiter = ",")
	
	
	for row in reader:
		keyDict.update({row['key']:row['value']})
		#print(keyDict)
		
	return keyDict
	
def convertFileToText(filepath): #takes a filepath for a .txt file and converts it to string
	file = open(filepath, 'r')
	contents = file.read()
	file.close()
	return contents
	
def fixText(text): #fixes commas and single quotes in the text for use with the plugboard
	newText = ""
	for letter in text:
		if letter == ",":
			letter = "/"
		elif letter == "\'":
			letter = "#"
		newText += letter
		
	return newText 
		
			
		
	
