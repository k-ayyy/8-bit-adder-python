#Code by: Kiran Khadka (19033683)
#code for bit adder

import gates as ckt  #importing for functionality

def bitAdder(binNum1, binNum2): 
       c_In=0
       c_Out=0
       index=-1
       aList=[]

       #loop to get 8 bit 
       for i in range (len(binNum1)):
              for j in range (len(binNum2)):
                     a=binNum1[index]  
                     b=binNum2[index]
                     
                     xorVal=ckt.XOR_Gate(a, b)  #call XOR_Gate function from ckt module

                     nandVal=ckt.NAND_Gate(xorVal,c_In)   #for inputs in nand gate

                     orVal=ckt.OR_Gate(xorVal,c_In)       #for inputs in or gate

                     sum_=ckt.AND_Gate(nandVal,orVal)     #for inputs in and gate

                     and1_Val=ckt.AND_Gate(a,b)           #for inputs in and gate

                     and2_Val=ckt.AND_Gate(xorVal,c_In)   #for inputs in next and gate

                     norVal=ckt.NOR_Gate(and1_Val,and2_Val)#for inputs in nor gate

                     c_Out=ckt.NOT_Gate(norVal)            #for input in not gate

                     c_In=c_Out #update carry values

                     aList.append(sum_) #add sum_ to aList
                     index= index -1   #re-declare index

              bList=[]  #create new list bList
              oppo=-1
              for k in range (len(aList)):  #get the numbers of characters in aList
                     bList.append(aList[oppo])
                     oppo=oppo-1
              return bList
                     
                     
       
