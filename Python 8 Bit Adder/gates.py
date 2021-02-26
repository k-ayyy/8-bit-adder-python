#Code by: Kiran Khadka (19033683)

#Code for gates

def XOR_Gate(p,q): #for xor gate 
    if (p!=q):
        return 1
    else:
        return 0
 

def AND_Gate(p,q):  #for and gate
    if p==1 and q==1:
        return 1
    else:
        return 0


def OR_Gate(p, q):  #for or gate
    if p==0 and q==0:
        return 0
    else:
        return 1


def NOT_Gate (p):   #for not gate
    if p==0:
        return 1
    else:
        return 0


def NAND_Gate (p,q): #for nand gate
    if p==1 and q==1:
        return 0
    else:
        return 1


def NOR_Gate (p,q):  #for nor gate
    if p==0 and q==0:
        return 1
    else:
        return 0
