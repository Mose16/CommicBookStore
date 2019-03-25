#File name
file = open("python.txt", "r")




###---Functions---###
def readFileLines(file):
    lines = file.readlines()
    return lines     
    
def createFile(fileName, text):
    newFile = open(fileName + ".txt", "w+")
    newFile.write(text)
    return

def addPass(line):
    if line.find("def ") != -1:
        pass
    elif line.find("class ") != -1:
        pass
    else:
        return line
    
    if line.find("()") == -1:
        pos = line.find("(") + 1
        line = line[:pos] + "Passing variables: " + line[pos:]
    
    return line    
    
        
def wordReplace(line):
    for word in WORDS:
        if word[:3] == " = ":
            if line.find(word) != -1:
                pos = line.find(word)
                line = PSEUDO[word] + line[:pos] + " to: " + line[pos + len(word) - 1:]
                
        else:
            if line.find(word) != -1:
                pos = line.find(word)
                
                line = line[:pos] + PSEUDO[word] + line[pos + len(word) - 1:]
    return line
        
            
        

###---Variables---###
PSEUDO = {
    "def ":"Define function called",
    "class ":"Define class called",
    " = ":"Set variable ",
}

WORDS = [
    "def ",
    "class ",
    " = "
]





###-------Main Code-------###
lines = readFileLines(file)
newFile = ""
for line in lines:
    line = addPass(line)
    line = wordReplace(line)
    
    newFile += "" + line

print(newFile)



createFile("generatedFile", newFile)
    