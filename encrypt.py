# Opening and reading the input file
file = input("What is the name of the file you would like to encrypt:")
ext = file[-4:]
if ext == ".png":

    with open(file, "rb") as imageFile:
        import binascii
        inText = (imageFile.read())
        print(inText)
        i = binascii.hexlify(inText)
        inText = str(inText)
        inText = inText[2:]
        inText = inText[:-1]

elif ext == ".txt":
    inFile = open(file, "r")
    inText = inFile.read()
    inFile.close()

else:
    print("File type not supported\n")
    quit()
print(inText)

# Add padding to the text file in the form of whitespace and convert to a matrix format
padNum = 5 - (len(inText) % 5)
if padNum == 5:
    padNum = 0
for i in range(padNum):
    inText = inText + ' '
textMat = []
i = 0
for j in range(int(len(inText) / 5)):
    a = []
    for k in range(5):
        a.append(inText[i])
        i = i + 1
    textMat.append(a)

# Ask for password
pas = input("Input a four digit password:")
try:
    int(pas)
except:
    print("This password will not work.")
    quit()
if len(pas) != 4:
    print("This password will not work.")
    quit()

newMat = []
rowNum = int(len(inText) / 5)

# Modify matrix based on password (part 1)
pasOne = int(pas[1])
for j in range(pasOne):
    if j != 0:
        textMat = newMat
        newMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = list(textMat[i - (rowNum-1)][0]) + textMat[i][1:]
        else:
            a = list(textMat[i + 1][0]) + textMat[i][1:]
        newMat.append(a)

textMat = newMat
newMat = []

# Modify matrix based on password (part 2)
pasTwo = int(pas[3])
for j in range(pasTwo):
    if j != 0:
        textMat = newMat
        newMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = list(textMat[i][0] + textMat[i - (rowNum-1)][1]) + textMat[i][2:]
        else:
            a = list(textMat[i][0] + textMat[i + 1][1]) + textMat[i][2:]
        newMat.append(a)

textMat = newMat
newMat = []

# Modify matrix based on password (part 3)
pasThree = int(pas[0])
for j in range(pasThree):
    if j != 0:
        textMat = newMat
        newMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = textMat[i][:2] + list(textMat[i - (rowNum-1)][2]) + textMat[i][3:]
        else:
            a = textMat[i][:2] + list(textMat[i + 1][2]) + textMat[i][3:]
        newMat.append(a)

textMat = newMat
newMat = []

# Modify matrix based on password (part 4)
pasFour = int(pas[2])
for j in range(pasFour):
    if j != 0:
        textMat = newMat
        newMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = textMat[i][:3] + list(textMat[i - (rowNum-1)][3]) + list(textMat[i][4])
        else:
            a = textMat[i][:3] + list(textMat[i + 1][3]) + list(textMat[i][4])
        newMat.append(a)

textMat = newMat
newMat = []

# Modify matrix based on coded standard (part 5)
for j in range(3):
    if j != 0:
        textMat = newMat
        newMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = textMat[i][:4] + list(textMat[i - (rowNum-1)][4])
        else:
            a = textMat[i][:4] + list(textMat[i + 1][4])
        newMat.append(a)
for row in newMat:
    print(row)

# Combine results in a list
outList = []
for row in newMat:
    outList.extend(row)

# Further modify the output by changing the ascii values based on the first and third value in the password
ascMod = pasFour * pasThree
i = 0
for ele in outList:
    outList[i] = chr(ord(ele) + ascMod)
    i += 1

# Turn list into a string and write to file
outString = "".join(outList)

if ext == ".png":
    outFile = open("output.png", "w")
    outFile.write(outString)
if ext == ".txt":
    outFile = open("output.txt", "w")
    outFile.write(outString)
outFile.close()
