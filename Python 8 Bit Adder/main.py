#Code by: Kiran Khadka (19033683)

#Code for main function(input and output)
import gates as ckt
import conversion
import adderfile



def main():
       ringroad=True 
       while ringroad==True:
              run1=True
              while run1==True:
                     try:
                            num1=int(input("Enter the first number here(0-255):"))
                            if num1 < 0 or num1 > 255:
                                   print("Sorry! Minimum 0 to maximum 255 acceptable only. " +"\n")
                            else:
                                   run1=False
                                   
                     except:
                            print("Validity Error! Please enter the number only." +"\n")
                            run1=True
                            
              run2=True         
              while run2==True:
                     try:
                            num2 =int(input("Enter the second number here(0-255):"))
                            if num2 < 0 or num2 > 255:
                                   print("Sorry! Minimum 0 to maximum 255 acceptable only." +"\n")
                                   break
                            else:
                                   run2=False
                                   
                     except:
                            print("Validity Error! Please enter the number only." +"\n")
                            run2=True
                            break
                            
                        
                     #call decimalToBinary function from conversion module to convert into binary 
                     binNum1= conversion.decimalToBinary(num1)
                     binNum2 = conversion.decimalToBinary(num2)
                     print("--------------------------------------------------------- \n")
                     print("The binary conversion of {} is: {}\n".format(num1,binNum1))
                     print("The binary conversion of {} is: {}\n".format(num2,binNum2))

                     #call str_ function from conversion module to get binary format string
                     strN1=conversion.str_(binNum1)
                     strN2=conversion.str_(binNum2)

                     #for bit adder
                     adderSum=[]
                     adderSum=adderfile.bitAdder(binNum1,binNum2)
                     print("The binary addition of the decimal numbers {} and {} is: ".format(num1, num2),adderSum)


                     #call binaryToDecimal function from conversion module to convert in to decimal
                     deciSum= conversion.binaryToDecimal(adderSum)
                     print("\n")
                     print("The decimal conversion of {} is: ".format(adderSum),deciSum)
                     print("---------------------------------------------------------- \n")



                     #asking for continue
                     pheriCon=input("Would you  love to continue? (Yes/No): ").lower()
                     if pheriCon =="no":
                            print("\n")
                            print("Have a nice day!  Thank you")
                            print("Visit us next time.")
                            ringroad=False
                            break
                         
                     else:
                            print("\n")
                            print("********************************************")
                            print("Carry on with the next inputs.")
                            print("*********************************************")
                     
                     
#execute main function everytime
if __name__=="__main__":
    main()
