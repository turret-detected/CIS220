#Author: Andrew Mohnkern, Zach Page
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: fileprovider.py
#Desc: Provides GUI based file selection functions

from tkinter import filedialog
from tkinter import *
import tkinter
import csv
import plugboard
import plug1


def getKeyFilePath(): #opens GUI file selector for a .csv key file
	keyFile = Tk()
	keyFile.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select key file",filetypes = (("csv files","*.csv"),("all files","*.*")))
	return keyFile.filename
	keyFile.destroy()
	
	
def getTextFilePath(): #opens a GUI file selector for a .txt file
	textFile = Tk()
	textFile.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select text file",filetypes = (("text files","*.txt"),("all files","*.*")))
	return textFile.filename
	#textFile.destroy()
	
def getSaveFilePath(): #opens a GUI save file window
	saveFilePath = Tk()
	saveFilePath.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Save text file",filetypes = (("text files","*.txt"),("all files","*.*")))
	return saveFilePath.filename
	
	
def convertCSVToDict(filepath): #converts a .csv file to a dict
	keyDict = {}
	reader = csv.DictReader(open(filepath, 'r'), delimiter = ",")
	
	
	for row in reader:
		keyDict.update({row['key']:row['value']})
		#print(keyDict)
		
	return keyDict
	
def convertFileToText(filepath): #takes a filepath for a .txt file and converts it to string
	currentfile = open(filepath, 'r')
	contents = currentfile.read()
	currentfile.close()
	return contents
	
def convertTextToFile(filepath, stringToSave): #takes a file path and a string, puts into file
	if '.txt' in filepath:
		currentfile = open(filepath, 'w+')
	else:
		currentfile = open(filepath+'.txt', 'w+')
	
	currentfile.write(stringToSave)
	currentfile.close()
	
def fixedPlugboard(plugDict=plugboard.getPlugboard()): #WIP adjusts plugboard to handle commas and quotes
	currentDict = plugDict
	
	for i in currentDict.keys():
		if i == "/":
			#i = ","
			currentDict.update({',':currentDict["/"]})
		elif i == "#":
			#i = '"'
			currentDict.update({'"':currentDict["#"]})

			
	for i in currentDict:
		if i == "/":
			#i = ","
			dictionary
			currentDict.update({KEY:','})
			
		elif i == "#":
			#i = '"'
			currentDict.update({KEY:'"'})
			
	return currentDict
	
def fixTextEncrypt(text): #fixes commas and single quotes in the text for use with the plugboard
	newText = ""
	for letter in text:
		if letter == ",":
			letter = "/"
		elif letter == "\'":
			letter = "#"
		newText += letter
		
	return newText 
	
def fixTextDecrypt(text):
	newText = ""
	for letter in text:
		if letter == "/":
			letter = ","
		elif letter == "#":
			letter = "'"
		newText += letter
		
	return newText
	
def encryptText():
	fileToEncrypt = getTextFilePath() #get file path
	fileText = convertFileToText(fileToEncrypt) #file contents to string
	fixedText = fixTextEncrypt(fileText) #convert comma and single quote
		
	newText = plug1.translate(fixedText) #translate file
	saveFilePath = getSaveFilePath() #open gui to save file
	convertTextToFile(saveFilePath, newText)
	#return newText	
			
		
def testRun():
	test = getSaveFilePath()
	teststring = "BLAH BLAH BLAH BLAH \n BLAH BLAH BLAH"
	convertTextToFile(test, teststring)
