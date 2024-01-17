# 1.py:
# A python module that contains task:


abc = input('enter string to count the characters:')
count = 0
countedDict = {}
# lowercase or uppercase it as you wish:
xyz = abc.lower()

for i in xyz:
    if i != ' ':
        count += 1
        if i not in countedDict:
            countedDict[i] = 1
        else:
            countedDict[i] += 1
print('total words inside the strings: %d;\n'%(count), countedDict)
