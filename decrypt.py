# Opening and reading the input file
file = input("What is the name of the file you would like to decrypt:")
inFile = open(file, "r")
inText = inFile.read()
inFile.close()
print(inText)

# Ask for password
pas = input("Input a four digit password:")

pasOne = int(pas[1])
pasTwo = int(pas[3])
pasThree = int(pas[0])
pasFour = int(pas[2])

inText = list(inText)
ascMod = pasFour * pasThree
i = 0
for ele in inText:
    inText[i] = chr(ord(ele) - ascMod)
    i += 1

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


newMat = textMat
rowNum = int(len(inText) / 5)

# Decryption of part 5
outMat = []
for j in range(3):
    if j != 0:
        newMat = outMat
        outMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = textMat[i][:4] + list(newMat[i - (rowNum+1)][4])
        else:
            a = textMat[i][:4] + list(newMat[i - 1][4])
        outMat.append(a)
newMat = outMat
outMat = []

# Decryption of part 4
for j in range(pasFour):
    if j != 0:
        newMat = outMat
        outMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = textMat[i][:3] + list(newMat[i - (rowNum+1)][3]) + list(newMat[i][4])
        else:
            a = textMat[i][:3] + list(newMat[i - 1][3]) + list(newMat[i][4])
        outMat.append(a)
newMat = outMat
outMat = []

# Decryption of part 3
for j in range(pasThree):
    if j != 0:
        newMat = outMat
        outMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = textMat[i][:2] + list(newMat[i - (rowNum+1)][2]) + newMat[i][3:]
        else:
            a = textMat[i][:2] + list(newMat[i - 1][2]) + newMat[i][3:]
        outMat.append(a)
newMat = outMat
outMat = []

# Decryption of part 2
for j in range(pasTwo):
    if j != 0:
        newMat = outMat
        outMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = list(textMat[i][0] + newMat[i - (rowNum+1)][1]) + newMat[i][2:]
        else:
            a = list(textMat[i][0] + newMat[i - 1][1]) + newMat[i][2:]
        outMat.append(a)
newMat = outMat
outMat = []

# Decryption of part 1
for j in range(pasOne):
    if j != 0:
        newMat = outMat
        outMat = []
    for i in range(rowNum):
        if i >= (rowNum - 1):
            a = list(newMat[i - (rowNum+1)][0]) + newMat[i][1:]
        else:
            a = list(newMat[i - 1][0]) + newMat[i][1:]
        outMat.append(a)
print('\n')
for row in outMat:
    print(row)

outString = []
for row in outMat:
    outString.extend(row)
outString = "".join(outString)
outFile = open("output.txt", "w")
outFile.write(outString.strip())
