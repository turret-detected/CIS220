

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
	appMain.setBg("cyan")
	
	
	#TOP
	appMain.startFrame("TOP", row=0, column=0, colspan=2) #centered top frame
	
	appMain.addLabel("title", "Enigma")
	appMain.setLabelBg("title", "cyan")
	appMain.getLabelWidget("title").config(font=("Arial 28"))
	
	#appMain.addImage("banner", "Assets/banner.gif")
	
	appMain.stopFrame()
	
	#MIDDLE LEFT
	appMain.startFrame("MIDDLE_LEFT", row=1, column=0)
	
	appMain.addLabel("InputFile", "")
	appMain.addLabel("OutputFile", "")
	appMain.getLabelWidget("InputFile").config(font=("Arial 16"))
	appMain.getLabelWidget("OutputFile").config(font=("Arial 16"))
	appMain.setLabelAlign("InputFile", "left")
	appMain.setLabelAlign("OutputFile", "left")
	appMain.setLabelPadding("InputFile", [20, 0])
	appMain.setLabelPadding("OutputFile", [20, 0])
	
	appMain.stopFrame()
	
	
	#MIDDLE RIGHT
	appMain.startFrame("MIDDLE_RIGHT", row=1, column=1)
	
	def selectIn(): #file selection in
		FilePaths.InFilePath = utilities.getTextFilePath()
		null = FilePaths.checkInput()
		appMain.setLabel("InputFile", FilePaths.InFilePath)
	
	def selectOut(): #file selection out
		FilePaths.OutFilePath = utilities.getSaveFilePath()
		null = FilePaths.checkOutput()
		appMain.setLabel("OutputFile", FilePaths.OutFilePath)
	
	appMain.addButton("SelectIn", selectIn)
	appMain.addButton("SelectOut", selectOut)
	appMain.setButton("SelectIn", "Choose input file")
	appMain.setButton("SelectOut", "Choose output file")
	#appMain.setButtonPadding("SelectIn", [100, 0])
	#appMain.setButtonPadding("SelectOut", [100, 0])
	#appMain.setButtonAlign("SelectIn", "right")
	#appMain.setButtonAlign("SelectOut", "right")
	appMain.setButtonSticky("SelectIn", "")
	appMain.setButtonSticky("SelectOut", "")
	#appMain.setButtonStrech("SelectIn", "none")
	
	
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
			
	appMain.addButtons(["Encrypt", "Decrypt", "Quit"], mainButtons)
	
	appMain.stopFrame()
			
	#MUST BE AT BOTTOM
	appMain.go()
	
	
#DEBUG LINE
#run_gui()





