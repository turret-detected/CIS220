#Author: Andrew Mohnkern, Zach Page
#Date: 6/14/19
#Class: CIS 220
#Project: Enigma Encryptor
#Filename: utilities.py
#Desc: Provides GUI based file selection functions

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import tkinter
import csv
import plugboard
import plug1
import decrypter
import getpass
import charFunction

def getUserDesktop(): #returns the current users desktop
	currentuser = getpass.getuser()
	desktoppath = "C:/Users/" + currentuser + "/Desktop/"
	return desktoppath
	
def getUnencryptedChars(text):
	charlist = []
	finalcharlist = []
	
	for i in text:
		#print(i)
		charlist.append(charFunction.charFunction(i))
		
		
	for i in charlist:
		if i == " ":
			pass
			
		elif i == "\n":
			pass
			
		elif i == None:
			pass
			
		else:
			finalcharlist.append(i)
		
	#print("The following characters were not encrypted")	
	#print(finalcharlist)
	
	if finalcharlist != []:
		messagebox.showinfo("Warning, unencrypted characters", "The following characters were not encrypted:\n"+str(finalcharlist))
		
	
def getTextFilePath(): #opens a GUI file selector for a .txt file
	textFile = Tk()
	textFile.filename = filedialog.askopenfilename(initialdir = getUserDesktop(),title = "Select text file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileName = textFile.filename
	textFile.destroy()
	return fileName
	#Note to self, python ignores things after the return statement
	
def getSaveFilePath(): #opens a GUI save file window
	saveFilePath = Tk()
	saveFilePath.filename = filedialog.asksaveasfilename(initialdir = getUserDesktop(),title = "Save text file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileName = saveFilePath.filename
	saveFilePath.destroy()
	return fileName
	
def convertFileToText(filepath): #takes a filepath for a .txt file and converts its contents to string | Zach did this
	currentfile = open(filepath, 'r')
	contents = currentfile.read()
	currentfile.close()
	return contents
	
def convertTextToFile(filepath, stringToSave): #takes a file path and a string, puts into file
	if '.txt' in filepath:
		currentfile = open(filepath, 'w+')
	else:
		currentfile = open(filepath+'.txt', 'w+')
	
	#fixes space at new line
	newString = stringToSave.replace("\n ", "\n")
	
	currentfile.write(newString)
	
	currentfile.close()
	
def fixTextEncrypt(text): #fixes commas and single quotes in the text for use with the plugboard
	newText = ""
	for letter in text:
		if letter == ",":
			letter = "/"
		elif letter == "'":
			letter = "#"
		newText += letter
		
	return newText 
	
def fixTextDecrypt(text): #reverses commas and quotes
	newText = ""
	for letter in text:
		if letter == "/":
			letter = ","
		elif letter == "#":
			letter = "'"
		newText += letter
		
	return newText
	
def encryptText(give=False): #encrypt file OLD
	fileToEncrypt = getTextFilePath() #get file path
	fileText = convertFileToText(fileToEncrypt) #file contents to string
	fixedText = fixTextEncrypt(fileText) #convert comma and single quote
	
	newText = plug1.translate(fixedText) #translate file
	saveFilePath = getSaveFilePath() #open gui to save file
	convertTextToFile(saveFilePath, newText) #save text to file

def decryptText(): #decrypt file OLD
	invertDict = decrypter.invertedDict() #get inverted dict
	
	fileToDecrypt = getTextFilePath() #get file path
	fileText = convertFileToText(fileToDecrypt) #file contents to string
	convertedText = plug1.translate(fileText, invertDict) #translate file
	fixedText = fixTextDecrypt(convertedText) #convert slash and hash
	saveFilePath = getSaveFilePath() #gui to save file
	convertTextToFile(saveFilePath, fixedText) #save text to file
	
	
def encryptTextArgs(inputFile, outputFile): #GUI encrypt
	fileText = convertFileToText(inputFile) #file contents to string
	fixedText = fixTextEncrypt(fileText) #convert comma and single quote
	getUnencryptedChars(fixedText)
	newText = plug1.translate(fixedText) #translate file
	saveFilePath = outputFile #save file path from args
	convertTextToFile(saveFilePath, newText) #save text to file
	
def decryptTextArgs(inputFile, outputFile): #GUI decrypt
	invertDict = decrypter.invertedDict() #get inverted dict
	
	fileText = convertFileToText(inputFile) #file contents to string
	convertedText = plug1.translate(fileText, invertDict) #translate file
	fixedText = fixTextDecrypt(convertedText) #convert slash and hash
	saveFilePath = outputFile #save file path from args
	convertTextToFile(saveFilePath, fixedText) #save text to file