print("********* WELCOME TO RADISSON BLUE HOTEL***********")
class hotelfarecal():
    def __init__(self,rt='',s=0,r=0,p=0,t=0,a=1800,name='',address='',contact='',cindate='',coutdate='',rno=101):
        self.rt=rt
        self.r=r
        self.p=p
        self.t=t
        self.s=s
        self.a=a

        self.name=name
        self.address=address
        self.contact=contact
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    
    def cust_data(self):
        self.name=input("Enter Customer Name: ")
        self.address=input("Enter Customer's Address: ")
        self.contact=int(input("Enter Contact Number: "))
        self.cindate=input("Enter CheckIN Date: ")
        self.coutdate=input("Enter CheckOut Date: ")
        print("Room Number: ",self.rno)
    
    def room_rent(self):
        print("We have the following Rooms Available")

        print("1. Type A--> Rs. 6000 PN/-")
        print("2. Type B--> Rs. 5000 PN/-")
        print("3. Type C--> Rs. 4000 PN/-")
        print("4. Type D--> Rs. 3000 PN/-")

        x=int(input("Enter Your Choice: "))
        n=int(input("How many days you want to stay: "))
    
        if(x==1):
            print("You have opted Type A Room")
            self.s=6000*n
        elif(x==2):
            print("You have opted Type B Room")
            self.s=5000*n
        elif(x==3):
            print("You have opted Type B Room")
            self.s=4000*n
        elif(x==4):
            print("You have opted Type B Room")
            self.s=3000*n
        else:
            print("Please Select an Option")
        print("Your Room Rent is= ",self.s)
    
    def rest_bill(self):
        print("*****RESTAURANT MENU******")

        print("1. Water-->100/-\n2. Tea-->150/-\n3. Breakfast-->1500/-\n4.Lunch-->1800/-\n5. Dinner-->2500/-\n6. Exit\n")


        while(1):
            c=int(input("Choose Any Option to Order: "))

            if(c==1):
                d=int(input("Enter the Quantity to place: "))
                self.r=self.r+100*d
            elif(c==2):
                d=int(input("Enter the Quantity to place: "))
                self.r=self.r+150*d
            elif(c==3):
                d=int(input("Enter the Quantity to place: "))
                self.r=self.r+1500*d
            elif(c==4):
                d=int(input("Enter the Quantity to place: "))
                self.r=self.r+1800*d
            elif(c==5):
                d=int(input("Enter the Quantity to place: "))
                self.r=self.r+2500*d
            elif(c==6):
                break
            else:
                print("Choose an Option to Order")
        print("Your total bill is:",self.r)

    def lan_bill(self):
        print("*****LAUNDARY******")

        print("1. Shorts-->100/-\n2. Jeans-->450/-\n3. Trousers-->300/-\n4.shirts-->600/-\n5. Exit\n")

        while(1):
            k=int(input("Choose Any Option to Order: "))

            if(k==1):
                g=int(input("Enter the Quantity to place: "))
                self.t=self.t+100*g
            elif(k==2):
                g=int(input("Enter the Quantity to place: "))
                self.t=self.t+450*g
            elif(k==3):
                g=int(input("Enter the Quantity to place: "))
                self.t=self.t+300*g
            elif(k==4):
                g=int(input("Enter the Quantity to place: "))
                self.t=self.t+600*g
            elif(k==5):
                break
            else:
                print("Choose an Option:")
        print("Your total bill is:",self.t)


    def game_bill(self):
        print("*****Game MENU******")
        print("1. Table Tennis -->100/-\n2. Ice Hockey-->150/-\n3. Bike Racing-->500/-\n4. Shooting-->100/-\n5. Exit\n")

        while(1):
            f=int(input("Enter your Choices: "))

            if(f==1):
                h=int(input("Enter the hours Played: "))
                self.p=self.p+100*h
            elif(f==2):
                h=int(input("Enter the hours Played: "))
                self.p=self.p+150*h
            elif(f==3):
                h=int(input("Enter the hours Played: "))
                self.p=self.p+500*h
            elif(f==4):
                h=int(input("Enter the hours Played: "))
                self.p=self.p+100*h
            elif(f==5):
                break
            else:
                print("Choose any Option: ")
        print("Your Total Bill is: ",self.p)


    def display(self):
        print("*****HOTEL BILL****")  
        print("Customer Details:")
        print("Customer Name",self.name)
        print("Customer Address",self.address)
        print("Customer Contact Number",self.contact)
        print("Check IN Date",self.cindate)
        print("Check Out Date",self.coutdate)
        print("Room No",self.rno)
        print("Total Room Rent:",self.s)
        print("Total Food Bill:",self.r)
        print("Total Laundary Bill: ",self.t)
        print("Total  Game bill: ",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print("Your Bill: ",self.rt)
        print("Additional Charges: ",self.a)
        print("Total Bill: ",self.rt+self.a)
        self.rno+=1
        # self.rt=self.s+self.t+self.p+self.r

def main():
    a=hotelfarecal()
    while(True):
        print("1. Enter Customer Data")
        print("2. Room Types")
        print("3. Restaurant Bill")
        print("4. Laundary Bill")
        print("5. Game Bill")
        print("6. Show Total Cost")
        print("7. EXIT")
        ch=int(input("\nENTER YOUR CHOICES: "))
        if(ch==1):
            a.cust_data()
        elif(ch==2):
            a.room_rent()
        elif(ch==3):
            a.rest_bill()
        elif(ch==4):
            a.lan_bill()
        elif(ch==5):
            a.game_bill()
        elif(ch==6):
            a.display()
        elif(ch==7):
            exit()
main()
