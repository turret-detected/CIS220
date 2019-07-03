

import utilities
from appJar import gui



def run_gui():
	#vars
	
	class FilePaths():
		
		InFilePath = ""
		OutFilePath = ""
			
		def areNull():
			if FilePaths.InFilePath == "":
				return True
			elif FilePaths.OutFilePath == "":
				return True
			else:
				return False


	#Main window
	appMain = gui("Enigma", "800x600")
	
	appMain.setBg("cyan")
	
	#TOP
	appMain.startFrame("TOP", row=0, column=0, colspan=2)
	appMain.addLabel("title", "Enigma")
	appMain.setLabelBg("title", "cyan")
	appMain.getLabelWidget("title").config(font=("Arial 28"))
	
	#appMain.addImage("banner", "Assets/banner.gif")
	
	appMain.stopFrame()
	
	

	
	#MIDDLE LEFT
	appMain.startFrame("MIDDLE_LEFT", row=1, column=0)
	
	appMain.addLabel("InputFile")
	appMain.addLabel("OutputFile")
	appMain.getLabelWidget("InputFile").config(font=("Arial 16"))
	appMain.getLabelWidget("OutputFile").config(font=("Arial 16"))
	appMain.setLabelAlign("InputFile", "left")
	appMain.setLabelAlign("OutputFile", "left")
	appMain.setLabelPadding("InputFile", [20, 0])
	appMain.setLabelPadding("OutputFile", [20, 0])
	
	appMain.stopFrame()
	
	
	#MIDDLE RIGHT
	appMain.startFrame("MIDDLE_RIGHT", row=1, column=1)
	def selectIn():
		FilePaths.InFilePath = utilities.getTextFilePath()
	
	def selectOut():
		FilePaths.OutFilePath = utilities.getSaveFilePath()
	
	appMain.addButton("SelectIn", selectIn)
	appMain.addButton("SelectOut", selectOut)
	#appMain.setButtonPadding("SelectIn", [100, 0])
	#appMain.setButtonPadding("SelectOut", [100, 0])
	#appMain.setButtonAlign("SelectIn", "right")
	#appMain.setButtonAlign("SelectOut", "right")
	appMain.setButtonSticky("SelectIn", "e")
	appMain.setButtonSticky("SelectOut", "e")



	
	appMain.stopFrame()
	
	
	
	#BOTTOM
	appMain.startFrame("BOTTOM", row=2, column=0, colspan=2)
	
	def encryptButton():
		if not FilePaths.areNull():
			utilities.encryptTextArgs(FilePaths.InFilePath, FilePaths.OutFilePath)
		else:
			print("ERROR")

	def decryptButton():
		if not FilePaths.areNull():
			utilities.decryptTextArgs(FilePaths.InFilePath, FilePaths.OutFilePath)
		else:
			print("ERROR")
	
	
	def mainButtons(button):
	
		#Encrypt
		if button == "Encrypt":
			encryptButton()
			
		#Decrypt
		elif button == "Decrypt":
			decryptButton()
			
	appMain.addButtons(["Encrypt", "Decrypt"], mainButtons)
	
	appMain.stopFrame()
			
	#MUST BE AT BOTTOM
	appMain.go()