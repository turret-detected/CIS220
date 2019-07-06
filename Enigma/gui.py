

import utilities
from appJar import gui



def run_gui():
	
	#static class to hold file paths
	class FilePaths():
		
		InFilePath = ""
		OutFilePath = ""
		
		def checkInput(): #returns false if input filepath is invalid, throws appropriate errorboxes
			InExt = FilePaths.InFilePath[-4:] #takes last four characters
			#print(InExt) #DEBUG
		
			if FilePaths.InFilePath == "":
				appMain.errorBox("Error", "You have not selected a file to encrypt.")
				return False
			
			elif InExt != ".txt":
				appMain.errorBox("Error", "Your input file must be a text file.")
				FilePaths.InFilePath = ""
				return False
				
			else:
				return True
				
		def checkOutput(): #returns false if output filepath is invalid, throws appropriate errorBoxes
			OutExt = FilePaths.OutFilePath[-4:] #takes last four characters
			
			if FilePaths.OutFilePath == "":
				appMain.errorBox("Error", "You have not selected a file to output to.")
				return False
			
			elif OutExt != ".txt":
				appMain.errorBox("Error", "Your output file must be a text file.")
				FilePaths.OutFilePath = ""
				return False
				
			else:
				return True
			
			
	#Main window
	appMain = gui("Enigma", "800x600")
	appMain.setTitle("Enigma Machine")
	appMain.setIcon("assets/icon.gif") #does not work for some reason
	appMain.setBg("#6B7A8F")
	appMain.setFont(family="Verdana")
	
	
	#TOP
	appMain.startFrame("TOP", row=0, column=0, colspan=2) #centered top frame
	appMain.setBg("#6B7A8F")
	appMain.addImage("banner", "assets/banner.gif")
	
	appMain.stopFrame()
	
	#MIDDLE LEFT
	appMain.startFrame("MIDDLE_LEFT", row=1, column=0)
	#appMain.setBg("#6B7A8F")
	
	appMain.addLabel("InputFile", "")
	appMain.addLabel("OutputFile", "")
	appMain.getLabelWidget("InputFile").config(font=("Verdana 14"))
	appMain.getLabelWidget("OutputFile").config(font=("Verdana 14"))
	appMain.setLabelAlign("InputFile", "left")
	appMain.setLabelAlign("OutputFile", "left")
	appMain.setLabelPadding("InputFile", [20, 0])
	appMain.setLabelPadding("OutputFile", [20, 0])
	
	#color
	appMain.setLabelFg("InputFile", "white")
	appMain.setLabelFg("OutputFile", "white")
	
	appMain.stopFrame()
	
	
	#MIDDLE RIGHT
	appMain.startFrame("MIDDLE_RIGHT", row=1, column=1)
	#appMain.setBg("#DCC7AA")
	
	#Button funcs
	def selectIn(): #file selection in
		FilePaths.InFilePath = utilities.getTextFilePath()
		null = FilePaths.checkInput()
		appMain.setLabel("InputFile", FilePaths.InFilePath)
	
	def selectOut(): #file selection out
		FilePaths.OutFilePath = utilities.getSaveFilePath()
		null = FilePaths.checkOutput()
		appMain.setLabel("OutputFile", FilePaths.OutFilePath)
	
	#Selection buttons
	appMain.addButton("SelectIn", selectIn)
	appMain.addButton("SelectOut", selectOut)
	appMain.setButton("SelectIn", "Choose input file")
	appMain.setButton("SelectOut", "Choose output file")
	appMain.setButtonSticky("SelectIn", "")
	appMain.setButtonSticky("SelectOut", "")

	#Color
	appMain.setButtonFg("SelectIn", "white")
	appMain.setButtonBg("SelectIn", "#F7882F")
	appMain.setButtonFg("SelectOut", "white")
	appMain.setButtonBg("SelectOut", "#F7882F")
	
	
	appMain.stopFrame()
	
	#BOTTOM
	appMain.startFrame("BOTTOM", row=2, column=0, colspan=2) #centered bottom frame
	
	def encryptButton():
		if FilePaths.checkInput():
			if FilePaths.checkOutput(): #check in and out, just in case
				utilities.encryptTextArgs(FilePaths.InFilePath, FilePaths.OutFilePath)
				appMain.infoBox("Done", "Encryption complete")
			
	def decryptButton():
		if FilePaths.checkInput():
			if FilePaths.checkOutput(): #check in and out, just in case
				utilities.decryptTextArgs(FilePaths.InFilePath, FilePaths.OutFilePath)
				appMain.infoBox("Done", "Decryption complete")


	def mainButtons(button):
		#Encrypt
		if button == "Encrypt":
			encryptButton()
			
		#Decrypt
		elif button == "Decrypt":
			decryptButton()
			
		#Quit	
		elif button == "Quit":
			appMain.stop()
			print("Application quit.")
		
	buttonList = ["Encrypt", "Decrypt", "Quit"]
		
	appMain.addButtons(buttonList, mainButtons)
	
	#Color
	for i in buttonList:
		appMain.setButtonFg(i, "white")
		appMain.setButtonBg(i, "#F7882F")
	
	appMain.stopFrame()
			
	#MUST BE AT BOTTOM
	appMain.go()
	
	
#DEBUG LINE
#run_gui()





