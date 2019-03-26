#File name
file = open("python.txt", "r")

#Controls:
xPass = True
xAnd = True
xQuotes = False




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

def repAnd(line):
    if line.find(", ") != -1:
        pos = line.rfind(", ")
        line = line[:pos] + " and" + line[pos + 1:]
    return line

def removeQuotes(line):
    progress = 0
    while line[progress:].find("\"") != -1:
        pos = line.find("\"", progress)
        line = line[:pos] + line[pos + 1:]
        progress = pos  
    return line
              
def wordRep(line):
    for word in WORDS:
        if word[:3] == " = ":
            if line.find(word) != -1:
                pos = line.find(word)
                             
                if line.rfind(" ", 0, pos) != -1:
                    start = line.rfind(" ", 0, pos)
                else:
                    start = 0
                print(start)
                line = line[:start] + PSEUDO[word] + line[start:pos] + "' to: " + line[pos + len(word):]
    
        if word == "def " or word == "class " or word == "def __init__":
            if line.find(word) != -1:
                pos = line.find(word)
                line = line[:pos] + PSEUDO[word] + line[pos + len(word):]
                
                while line.find(" = ") != -1:
                    pos = line.find(" = ")
                    start = line.rfind(", ", 0, pos)
                    if line.find(", ", pos) != -1:
                        end = line.find(", ", pos)
                    else:
                        end = line.find("):", pos)
                    line =  line[:start + 2] + "(Set variable '" + line[start + 2:pos] + "' to " + line[pos + 3:end] + " by default)" + line[end:]
        else:
            if line.find(word) != -1:
                pos = line.find(word)
                
                line = line[:pos] + PSEUDO[word] + line[pos + len(word):]                

    return line
        
            
        

###---Variables---###
PSEUDO = {
    "def ":"Define a function called ",
    "class ":"Define a class called ",
    " = ":"Set variable '",
    "pass":"Do nothing ",
    "def __init__":"Define object constructor function"
}

WORDS = [
    "def __init__",
    "def ",
    "class ",
    " = ",
    "pass"    
]





###-------Main Code-------###
lines = readFileLines(file)
newFile = ""
for line in lines:
    line = wordRep(line)
    
    #Conditionals
    if xPass:
        line = addPass(line)
    if xAnd:
        line = repAnd(line)
    if xQuotes:
        line = removeQuotes(line)
    
    newFile += line

print(newFile)



createFile("generatedFile", newFile)