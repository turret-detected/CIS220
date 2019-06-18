#Author: Andrew Mohnkern, Zach Page
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: fileprovider.py
#Desc: Provides GUI based file selection functions


from tkinter import filedialog
from tkinter import *
import csv


def getKeyFilePath():
	keyFile = Tk()
	keyFile.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select key file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	return keyFile.filename
	keyFile.destroy()

def getTextFilePath():	
	textFile = Tk()
	textFile.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select text file",filetypes = (("text files","*.txt"),("all files","*.*")))
	return textFile.filename
	textFile.destroy()
	
def convertCSVToDict(filepath):
	keyDict = {}
	reader = csv.DictReader(open(filepath, 'r'), delimiter = ",")
	
	
	for row in reader:
		keyDict.update({row['key']:row['value']})
		#print(keyDict)
		
	return keyDict
	
def convertFileToText(filepath):
	file = open(filepath, 'r')
	contents = file.read()
	file.close()
	return contents
	
