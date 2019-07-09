import plugboard

newDict = plugboard.getPlugboard()
#print(newDict)

def charFunction(newChar):
    if newChar not in newDict:
        return newChar
