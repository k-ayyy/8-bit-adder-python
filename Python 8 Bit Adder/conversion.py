#Code by: Kiran Khadka (19033683)
#code for binary conversion of the user input


def decimalToBinary(decimalNum):
     bitBox = []  #create list bitBox
     remainder=0  #declare remainder and initialize to 0
     index=-1
     binList=[]   #create list binList
     for i in range(8):
          remainder = decimalNum%2
          bitBox.append(remainder)
          decimalNum=decimalNum//2
     for j in range(len(bitBox)):
          binList.append(bitBox[index])
          index-=1
     return binList



#code for binary format string
def str_(binList):
     strList=[]
     for y in range(len(binList)):
          z=str(binList[y])
          strList.append(z)

     strFormat=''.join(strList) #covert into string
     return strFormat




#code for decimal conversion
def binaryToDecimal(binList):
     dec=0
     index=-1
     for m in range(len(binList)):
          n=binList[index]
          dec= dec+n*(2**m)
          index-=1
     return dec


