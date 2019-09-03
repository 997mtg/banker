import os

def cls():
    return print(os.system("cls"))
    
def mainmenu():
    cls()
    print("Bank Manager v2.0\n\nMAIN MENU\n  1  Create new account\n  2  Info on an account\n  3  Transaction\n  4  Modify account\n  5  EXIT")

class account():
    def __init__(self, name, amount, id):
        self.name=name
        self.amount=amount
        self.id=id
    
    def saveacc(self):
        accdata=open("{}.txt".format(self.id), "w")
        accdata.write(self.id)
        accdata.write("\n")
        accdata.write(self.name)
        accdata.write("\n")
        accdata.write(self.amount)
        accdata.close()
        
    def getacc(self):
        lns=[]
        try:
            accdata = open("{}.txt".format(self.id), "r")
            lns = accdata.readlines()
            
            accdata.close()
            self.id=lns[0]
            self.name=lns[1]
            self.amount=lns[2]
        except FileNotFoundError: 
            print("Unable to find the account")
        return lns
    
    def modify(self, nid, nname, namount):
        self.name=nname
        self.id=nid
        self.amount=namount
        

menu=1
while menu!=0:
    mainmenu()
    menu=int(input())
    if menu == 1:
        cls()
        print("NEW ACCOUNT\n\n")
        name = input("   Name:")
        id = input("   ID:")
        amount = input("   Amount:")
        temp = account(name, amount, id)
        temp.saveacc()
    elif menu == 2:
        cls()
        print("INFO")
        id=input("\n\n   Search by ID:")
        temp = account("", "", id)
        lns=temp.getacc()
        print("ID:     {}".format(lns[0]))
        print("Name:   {}".format(lns[1]))
        print("Amount: {}".format(lns[2]))
        waitval=input()
    elif menu == 3:
        cls()
        print("TRANSACTION")
        id1 = input("\n\n   Enter payer's ID:")
        payer=account("","",id1)
        temp1=payer.getacc()
        id2 = input("   Enter payee's ID:")
        payee=account("","",id2)
        temp2=payee.getacc()
        amount=float(input("   Enter the amount:"))
        for i in range(len(temp1)):
            temp1[i] = temp1[i].strip()
        for i in range(len(temp2)):
            temp2[i] = temp2[i].strip()
        print(temp1[0])
        a1 = float(temp1[2])
        a2 = float(temp2[2])
        a1=a1-amount
        a2=a2+amount
        a1=str(a1)
        a2=str(a2)
        payer.modify(temp1[0], temp1[1], a1)
        payee.modify(temp2[0], temp2[1], a2)
        payer.saveacc()
        payee.saveacc()
        cls()
        print("\n\n\n      TRANSACTION SUCCESSFUL!")
        waitval=input()
    elif menu == 4:
        cls()
        print("Not available yet!")
        menu=0
    else: menu = 0
    
