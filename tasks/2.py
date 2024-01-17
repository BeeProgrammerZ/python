# 2.py:
# A python module that contains task:

duplicates = [1,1,2,2,3,3,4,4]
uniqueList = list()

for i in duplicates:
  if i not in uniqueList:
    uniqueList.append(i)
print('original list:',duplicates)
print('unique list:',uniqueList)
