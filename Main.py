from math import *
from math import log
from tkinter import *
from tkinter import ttk
import datetime
import tkinter as tk
from tkinter import messagebox
######################################---Maneger Class---########################
ManegerList = []
class Maneger:

    def __init__(self,identify,phoneNumber,name,userName,password):
        self.identify=identify
        self.name=name
        self.phoneNumber=phoneNumber
        self.userName=userName
        self.password=password
def CreateManeger():
        ##creat Maneger---one time
        maneger=Maneger("Maneger","0504747155","AmerAbuArar","amer","a")
        ManegerList.append(maneger)
        ManegerFile=open("Maneger.txt","w")
        for var in ManegerList:
                ManegerFile.writelines(var.identify)
                ManegerFile.writelines("|")
                ManegerFile.writelines(var.phoneNumber)
                ManegerFile.writelines("|")
                ManegerFile.writelines(var.name)
                ManegerFile.writelines("|")
                ManegerFile.writelines(var.userName)
                ManegerFile.writelines("|")
                ManegerFile.writelines(var.password)
                ManegerFile.writelines("\n")
        ManegerFile.close()
def ReadManegerFromFile():
        ManegerFile=open("Maneger.txt","r")
        for Line in ManegerFile:
                if Line[-1]=="\n":
                    Line=Line[0:len(Line)-1]
                Line=Line.split("|")
                i=0
                if i<len(Line):
                    maneger_identify=Line[i]
                    i=i+1
                    maneger_phoneNumber = Line[i]
                    i = i + 1
                    maneger_name = Line[i]
                    i = i + 1
                    maneger_userName = Line[i]
                    i = i + 1
                    maneger_password= Line[i]
                    i = i + 1


                    ManegerList.append( Maneger(maneger_identify,maneger_phoneNumber,maneger_name,maneger_userName,maneger_password))
        ManegerFile.close()
####################################################---Technician Class---########################
TechnicianList = []
class Technician:
    def __init__(self, identify, phoneNumber, name, userName, password,WorkHour,Location):
        self.identify = identify
        self.name = name
        self.phoneNumber = phoneNumber
        self.userName = userName
        self.password = password
        self.WorkHour=WorkHour
        self.Location=Location
def AddTechnicianListToTechnicianFile():

        TechnicianFile = open("Technician.txt", "w")
        for var in TechnicianList:
            TechnicianFile.writelines(var.identify)
            TechnicianFile.writelines("|")
            TechnicianFile.writelines(var.phoneNumber)
            TechnicianFile.writelines("|")
            TechnicianFile.writelines(var.name)
            TechnicianFile.writelines("|")
            TechnicianFile.writelines(var.userName)
            TechnicianFile.writelines("|")
            TechnicianFile.writelines(var.password)
            TechnicianFile.writelines("|")
            TechnicianFile.writelines(var.WorkHour)
            TechnicianFile.writelines("|")
            TechnicianFile.writelines(var.Location)
            TechnicianFile.writelines("\n")
        TechnicianFile.close()
def ReadTechnicianListFromTechnicianFile():
        TechnicianFile = open("Technician.txt", "r")
        for Line in TechnicianFile:
            if Line[-1] == "\n":
                Line = Line[0:len(Line) - 1]
            Line = Line.split("|")
            i = 0
            if i < len(Line):
                Technician_identify = Line[i]
                i = i + 1
                Technician_phoneNumber = Line[i]
                i = i + 1
                Technician_name = Line[i]
                i = i + 1
                Technician_userName = Line[i]
                i = i + 1
                Technician_password = Line[i]
                i = i + 1
                Technician_WorkHour = Line[i]
                i = i + 1
                Technician_Location = Line[i]
                i = i + 1

                TechnicianList.append(Technician(Technician_identify, Technician_phoneNumber, Technician_name, Technician_userName, Technician_password, Technician_WorkHour, Technician_Location ))
        TechnicianFile.close()
####################################################---Client Class---########################
ClientList = []
class Client:
    def __init__(self, identify, phoneNumber, name, userName, password,Location):
        self.identify = identify
        self.name = name
        self.phoneNumber = phoneNumber
        self.userName = userName
        self.password = password
        self.Location=Location
def AddClientListToClientFile():
        ClientFile = open("Client.txt", "w")
        for var in ClientList:
            ClientFile.writelines(var.identify)
            ClientFile.writelines("|")
            ClientFile.writelines(var.phoneNumber)
            ClientFile.writelines("|")
            ClientFile.writelines(var.name)
            ClientFile.writelines("|")
            ClientFile.writelines(var.userName)
            ClientFile.writelines("|")
            ClientFile.writelines(var.password)
            ClientFile.writelines("|")
            ClientFile.writelines(var.Location)
            ClientFile.writelines("\n")
        ClientFile.close()
def ReadClientListFromClientFile():
        ClientFile = open("Client.txt", "r")
        for Line in ClientFile:
            if Line[-1] == "\n":
                Line = Line[0:len(Line) - 1]
            Line = Line.split("|")
            i = 0
            if i < len(Line):
                Client_identify = Line[i]
                i = i + 1
                Client_phoneNumber = Line[i]
                i = i + 1
                Client_name = Line[i]
                i = i + 1
                Client_userName = Line[i]
                i = i + 1
                Client_password = Line[i]
                i = i + 1
                Client_Location = Line[i]
                i = i + 1

                ClientList.append(Client(Client_identify, Client_phoneNumber, Client_name, Client_userName, Client_password, Client_Location ))
        ClientFile.close()
####################################################---Product Class---########################
ProductList = []
class Product:
    def __init__(self,ProductCode,ProductName):
        self.ProductCode = ProductCode
        self.ProductName = ProductName
def AddProductListToProductFile():

        ProductFile = open("Product.txt", "w")
        for var in ProductList:
            ProductFile.writelines(var.ProductCode)
            ProductFile.writelines("|")
            ProductFile.writelines(var.ProductName)
            ProductFile.writelines("\n")
        ProductFile.close()
def ReadProductListFromProductFile():
        ProductFile = open("Product.txt", "r")
        for Line in ProductFile:
            if Line[-1] == "\n":
                Line = Line[0:len(Line) - 1]
            Line = Line.split("|")
            i = 0
            if i < len(Line):
                Product_ProductCode = Line[i]
                i = i + 1
                Product_ProductName = Line[i]
                i = i + 1


                ProductList.append(Product(Product_ProductCode, Product_ProductName ))
        ProductFile.close()
####################################################---ProductsPurchased Class---  ########################
ProductPurchasedList = []
class ProductPurchased:
    def __init__(self,PurchaseCode,ProductCode, ClientPhoneNumber,PurchaseDate,NextDateForMaintenance):
        self.PurchaseCode = PurchaseCode
        self.ProductCode = ProductCode
        self.ClientPhoneNumber = ClientPhoneNumber
        self.PurchaseDate = PurchaseDate
        self.NextDateForMaintenance = NextDateForMaintenance
def AddProductPurchasedListToProductPurchasedFile():

        ProductPurchasedFile = open("ProductsPurchased.txt", "w")
        for var in ProductPurchasedList:
            ProductPurchasedFile.writelines(str(var.PurchaseCode))
            ProductPurchasedFile.writelines("|")
            ProductPurchasedFile.writelines(var.ProductCode)
            ProductPurchasedFile.writelines("|")
            ProductPurchasedFile.writelines(var.ClientPhoneNumber)
            ProductPurchasedFile.writelines("|")
            ProductPurchasedFile.writelines(var.PurchaseDate)
            ProductPurchasedFile.writelines("|")
            ProductPurchasedFile.writelines(var.NextDateForMaintenance)
            ProductPurchasedFile.writelines("\n")
        ProductPurchasedFile.close()
def ReadProductPurchasedListFromProductPurchasedFile():
        ProductPurchasedFile = open("ProductsPurchased.txt", "r")
        for Line in  ProductPurchasedFile:
            if Line[-1] == "\n":
                Line = Line[0:len(Line) - 1]
            Line = Line.split("|")
            i = 0
            if i < len(Line):
                ProductPurchased_PurchaseCode = Line[i]
                i = i + 1
                ProductPurchased_ProductCode = Line[i]
                i = i + 1
                ProductPurchased_ClientPhoneNumber= Line[i]
                i = i + 1
                ProductPurchased_PurchaseDate = Line[i]
                i = i + 1
                ProductPurchased_NextDateForMaintenance = Line[i]
                i = i + 1

                ProductPurchasedList.append(ProductPurchased(ProductPurchased_PurchaseCode, ProductPurchased_ProductCode,ProductPurchased_ClientPhoneNumber,ProductPurchased_PurchaseDate,ProductPurchased_NextDateForMaintenance))
        ProductPurchasedFile.close()
####################################################---Defect Class--- ########################
FaultList = []
class Fault:
    def __init__(self,FaultCode,ProductCode,ClientPhoneNumber,TechnicianPhoneNumber,FaultDate,FaultType,FaultStatus,Description,TreatmentTime,Distance,assigningDate):
        self.FaultCode = FaultCode
        self.ProductCode = ProductCode
        self.ClientPhoneNumber = ClientPhoneNumber
        self.TechnicianPhoneNumber = TechnicianPhoneNumber
        self.FaultDate = FaultDate
        self.FaultType = FaultType
        self.FaultStatus = FaultStatus
        self.Description = Description
        self.TreatmentTime = TreatmentTime
        self.Distance=Distance
        self.assigningDate=assigningDate
def AddFaultListToFaultFile():
        FaultFile = open("Fault.txt", "w")
        for var in FaultList:
            FaultFile.writelines(str(var.FaultCode))
            FaultFile.writelines("|")
            FaultFile.writelines(str(var.ProductCode))
            FaultFile.writelines("|")
            FaultFile.writelines(var.ClientPhoneNumber)
            FaultFile.writelines("|")
            FaultFile.writelines(var.TechnicianPhoneNumber)
            FaultFile.writelines("|")
            FaultFile.writelines(var.FaultDate)
            FaultFile.writelines("|")
            FaultFile.writelines(var.FaultType)
            FaultFile.writelines("|")
            FaultFile.writelines(var.FaultStatus)
            FaultFile.writelines("|")
            FaultFile.writelines(var.Description)
            FaultFile.writelines("|")
            FaultFile.writelines(var.TreatmentTime)
            FaultFile.writelines("|")
            FaultFile.writelines(var.Distance)
            FaultFile.writelines("|")
            FaultFile.writelines(var.assigningDate)
            FaultFile.writelines("\n")
        FaultFile.close()
        FaultList.clear()
        ReadFaultListFromFaultFile()


def ReadFaultListFromFaultFile():
        FaultFile = open("Fault.txt", "r")
        for Line in   FaultFile:
            if Line[-1] == "\n":
                Line = Line[0:len(Line) - 1]
            Line = Line.split("|")
            i = 0
            if i < len(Line):
                Fault_FaultCode = Line[i]
                i = i + 1
                Fault_ProductCode = Line[i]
                i = i + 1
                Fault_ClientPhoneNumber= Line[i]
                i = i + 1
                Fault_TechnicianPhoneNumber = Line[i]
                i = i + 1
                Fault_FaultDate= Line[i]
                i = i + 1
                Fault_FaultType = Line[i]
                i = i + 1
                Fault_FaultStatus = Line[i]
                i = i + 1
                Fault_Description = Line[i]
                i = i + 1
                Fault_TreatmentTime = Line[i]
                i = i + 1
                Fault_Distance = Line[i]
                i = i + 1
                Fault_assigningDate = Line[i]
                i = i + 1
                FaultList.append( Fault( Fault_FaultCode, Fault_ProductCode,Fault_ClientPhoneNumber,Fault_TechnicianPhoneNumber,Fault_FaultDate,Fault_FaultType ,Fault_FaultStatus ,Fault_Description ,Fault_TreatmentTime,Fault_Distance,Fault_assigningDate))
        FaultFile.close()
#########################################################################################################  functions
lstTypes = ['Critical malfunction','Normal malfunction','Maintenance failure']
def TreatmentTimeForFaultType(FaultType):
    if (FaultType == lstTypes[0]):
        TreatmentTime = "2"
    if (FaultType == lstTypes[1]):
        TreatmentTime = "1"
    if (FaultType == lstTypes[2]):
        TreatmentTime = "0.5"
    return TreatmentTime
def CreateTechnician(phoneNumber, name, userName, password):
    t=Technician('Technician', phoneNumber, name, userName, password,'0',"(31.2525238,34.7905787)")
    TechnicianList.append(t)
    AddTechnicianListToTechnicianFile()
def AddClient(userName,password,phoneNumber,place,name, dateofbought, dateOfServicing,codeOfProduct):#add Client
    M=Client('Client',phoneNumber,name,userName,password,place)#object of Maneger type
    ClientList.append(M)
    if ProductPurchasedList == []:
        i = 23535
    else:
        i = int(ProductPurchasedList[len(ProductPurchasedList)-1] .PurchaseCode)+ 1
    Pp=ProductPurchased(i,codeOfProduct,phoneNumber,dateofbought,dateOfServicing)
    ProductPurchasedList.append(Pp)
    AddClientListToClientFile()
    AddProductPurchasedListToProductPurchasedFile()
def AddProducts(codeOfProduct,nameOfProduct):
    P=Product(codeOfProduct,nameOfProduct)
    ProductList.append(P)
    AddProductListToProductFile()
def CreateFault(ProductCode,ClientPhoneNumber,TechnicianPhoneNumber,FaultDate,FaultType,FaultStatus,Description,TreatmentTime,Distance,assigningDate):
    if FaultList == []:
        FaultCode = 4564
    else:
        FaultCode = int(FaultList[len(FaultList) - 1].FaultCode) + 1
    FaultList.append(Fault(FaultCode,ProductCode,ClientPhoneNumber,TechnicianPhoneNumber,FaultDate,FaultType,FaultStatus,Description,TreatmentTime,str(Distance),assigningDate))
    AddFaultListToFaultFile()
def DateToString():
    Date = datetime.date.today()
    DateDay = Date.day
    DateMonth = Date.month
    DateYear = Date.year
    return str(DateYear) + "-" + str(DateMonth) + "-" + str(DateDay)
def assigningDateUpdate():#every day we have anew  assigning
    DateForThisDay = DateToString()
    for Fault in FaultList:
        if Fault.assigningDate!=DateForThisDay and Fault.FaultStatus!="Done" :
            for Technician in TechnicianList:
                    Technician.WorkHour="0"
            Fault.TechnicianPhoneNumber="0"
            Fault.FaultStatus="New Fault"
            Fault.assigningDate="Not assigning yet"
dicLocation={}
def ReadFromLocationFile():
    LocationFile = open("Location.txt", "r")
    for Line in LocationFile:
        if Line[-1] == "\n":
            Line = Line[0:len(Line) - 1]
            Line = Line.split("|")
            dicLocation[Line[0]]="("+Line[1]+","+Line[2]+")"
def ReadFromFiles():
    ReadFromLocationFile()
    ReadManegerFromFile()
    ReadTechnicianListFromTechnicianFile()
    ReadClientListFromClientFile()
    ReadProductListFromProductFile()
    ReadProductPurchasedListFromProductPurchasedFile()
    ReadFaultListFromFaultFile()
def WriteToFiles():
    AddTechnicianListToTechnicianFile()
    AddClientListToClientFile()
    AddProductListToProductFile()
    AddProductPurchasedListToProductPurchasedFile()
    AddFaultListToFaultFile()
def CheckLogin(userName,passWord):
    for item in ManegerList:
        if(item.userName==userName and item.password==passWord):
            return item;
    for item in ClientList:
        if (item.userName == userName and item.password == passWord):
            return item;
    for item in TechnicianList:
        if (item.userName == userName and item.password == passWord):
            return item;
    return 0;
def Login_user():
    username_info = username.get()
    password_info = password.get()

    user=CheckLogin(username_info,password_info)
    if(user!=0):
        Label(Login_screen, text="Login Success", fg="green", font=("calibri", 11)).pack()
        Login_screen.destroy()
        if(user.identify=='Maneger'):
            # open screen manager
            ScreenManeger(user)

        elif(user.identify=='Technician'):
            FaultListForTechnician = []
            if FaultList!=[]:
                for i in range(len(FaultList)):
                    if FaultList[i].TechnicianPhoneNumber == user.phoneNumber:
                        FaultListForTechnician.append(i)
            if FaultListForTechnician!=[]:
                    screenTechnician(user,0)
            else:
                messagebox.showinfo("", "there is no assigning for you today:)")

        elif(user.identify=='Client'):
            #open screen clint
            count=0
            for item in ProductPurchasedList:
                if item.ClientPhoneNumber == user.phoneNumber:
                    count=count+1
            if count!=0:
                ScreenClient(user)
            else:
                messagebox.showinfo("", "you don't have Product:)")

    else:
        messagebox.showinfo("", "User Not Found")
def Login():
    global Login_screen
    Login_screen=Tk()
    Login_screen.title("Login")
    Login_screen.geometry("300x250+500+200")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(Login_screen, text="Please enter details below", bg="white").pack()
    Label(Login_screen, text="").pack()
    username_lable = Label(Login_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(Login_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(Login_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(Login_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(Login_screen, text="").pack()
    Button(Login_screen, text="Login", width=10, height=1, bg="gray", command=Login_user).pack()
    Login_screen.mainloop()
def ScreenClient(user):
    frmClient=Tk()
    frmClient.geometry("400x250+500+200")
    frmClient.title('Report')
    labName = Label(frmClient, text='Welcome'+' '+user.name,).grid(row=1, column=0)
    # function sends a list with ProductCode,ProductName
    def distance(scr, dist):
        x= scr.split(",")
        y = dist.split(",")
        x1 = x[0]
        x2 = x[1]
        xh = int(x1[-1])
        xg = int(x2[0])
        y1 = y[0]
        y2 = y[1]
        yh = int(y1[-1])
        yg = int(y2[0])
        dist = sqrt(pow(yh - xh,2) + pow(yg - xg,2) )
        return dist


    def ProductClient():
        listProductClient=[]
        for item in ProductPurchasedList:
            if item.ClientPhoneNumber == user.phoneNumber:
                for itemName in ProductList:
                    if itemName.ProductCode == item.ProductCode:
                        listProductClient.append(itemName.ProductName)
        return listProductClient
    ListNameOfProduct = ProductClient()
    Label(frmClient, text='    ').grid(row=5,column=0)
    Label(frmClient, text='Choose a Products').grid(row=7,column=0)
    var=StringVar()
    lst=[]
    def Selected(events):
        global saveSelected
        saveSelected=lst[pro.current()]
    for item in ListNameOfProduct:
        if item not in lst:
            lst.append(item)
    pro = ttk.Combobox(frmClient, values=lst,width=15, textvariable=var)
    pro.bind("<<ComboboxSelected>>",Selected)
    pro.current(0)
    pro.grid(column=1, row=7)

    def checkCodeOfProduct():
        for itemName in ProductList:
            if itemName.ProductName == saveSelected:
                code = itemName.ProductCode
        return code

    Label(frmClient, text='    ').grid(row=8, column=0)
    Label(frmClient, text='Choose a Type Of Fault').grid(row=9, column=0)

    def SelectedType(events):
        global saveSelectedType
        saveSelectedType = lstTypes[Type.current()]



    Type = ttk.Combobox(frmClient, values=lstTypes, width=15)
    Type.delete(0, END)
    Type.insert(0, lstTypes[1])
    Type.bind("<<ComboboxSelected>>", SelectedType)
    Type.current(0)

    Type.grid(column=1, row=9)

    def click_me():
            TreatmentTime=TreatmentTimeForFaultType(saveSelectedType)
            CreateFault(checkCodeOfProduct(),user.phoneNumber,"0",DateToString(),saveSelectedType,'New Fault',(e1.get()),TreatmentTime,distance(user.Location,'(31.2525238,34.7905787)'),"Not assigning yet")
            messagebox.showinfo("", "Add Fault Successful ")
            frmClient.destroy()
            Login()



    Label(frmClient, text='    ').grid(row=10, column=0)
    tk.Label(frmClient,text="Description").grid(row=11)
    e1 = tk.Entry(frmClient)
    e1.grid(row=11, column=1)
    tk.Button(frmClient,text='Send',width=10, command=click_me).grid(row=12,column=1,sticky=tk.W,pady=4)

    frmClient.mainloop()
def strToInt(number):
    if("." in number):
        number = number.split(".")
        x = number[0]
        y = number[1]
        lene = len(y)
        new = "1"
        for i in range(lene):
            new = new + "0"
        y = int(y) / int(new)
        number = int(x) + y
    else:
        number=int(number)
    return number
def DistanceKmInHours(dist):
    dist=strToInt(dist)
    x = dist/ 30
    y = x * 60
    y=y/60
    return y
import random
def assigningAutomaticByFaultType(FaultType):
    if(TechnicianList!=[]):
        TechnicianNumber=len(TechnicianList)-1
        if(TechnicianNumber>0):
            index=random.randrange(TechnicianNumber)
        else:
            index=0
        for Fault in FaultList:
            if(Fault.FaultType==FaultType):
                if(Fault.TechnicianPhoneNumber=='0'):
                    cal=strToInt(Fault.TreatmentTime)+DistanceKmInHours(Fault.Distance)+strToInt(TechnicianList[index].WorkHour)
                    if(cal<=8):
                        Fault.TechnicianPhoneNumber=TechnicianList[index].phoneNumber
                        TechnicianList[index].WorkHour=str(round(cal,2))
                        Fault.FaultStatus='In Progress'
                        Fault.assigningDate=DateToString()
def assigningAutomatic():
    assigningAutomaticByFaultType('Critical malfunction')
    assigningAutomaticByFaultType('Normal malfunction')
    assigningAutomaticByFaultType('Maintenance failure')
    WriteToFiles()
def ScreenManeger(user):
    def exit():
        frmManeger.destroy()
        Login()

    frmManeger=Tk()
    frmManeger.geometry("300x250+500+200")
    frmManeger.title('Maneger')
    labName = Label(frmManeger, text='Welcome'+' '+user.name, font='arial 10',fg='black' ).grid(row=3, column=0)
    ButtonForassigning = Button(frmManeger,text= "Assigning",command=assigningAutomatic).grid(row=5,column=0,pady=10,padx=100)
    ButtonAddClient = Button(frmManeger,text= "Add Client",command=ScreenAddClient).grid(row=7,column=0,pady=10,padx=100)
    ButtonAddProduct = Button(frmManeger,text= "Add Product",command=ScreenAddProdect).grid(row=9,column=0,pady=10,padx=100)
    ButtonAddTechnician = Button(frmManeger,text= "Add Technician",command=ScreenAddTechnician).grid(row=13,column=0,pady=10,padx=100)
    ButtonAddTechnician = Button(frmManeger,text= "Exit",command=exit).grid(row=15,column=0,pady=10,padx=100)
    frmManeger.mainloop()
def checkPhoneNumber(PhoneNumber):
    if len(PhoneNumber) == 10:
        if PhoneNumber.isdigit():
            return 1
        else:
            messagebox.showinfo("Wrong", "Phone Number Must Be 10 Number")
            return 0

    else:
        messagebox.showinfo("Wrong", "Phone Number Must Be 10 Number")
        return 0
def checkName(Name):
    for i in Name:
        if ((i<'a'or i>'z')and(i<'A'or i>'Z')):
            messagebox.showinfo("Wrong ", "Name Must Be letters")
            return 0
    return 1
def checkNotExistPhoneNumber(phoneNumber,list):
    l=[]
    for var in list:
        l.append(var.phoneNumber)
    if phoneNumber  not in l:
        messagebox.showinfo("Wrong ", "Phone Number is not Exist")
        return 0
    return 1
def checkExistPhoneNumber(phoneNumber,list):
    l=[]
    for var in list:
        l.append(var.phoneNumber)
    if phoneNumber  in l:
        messagebox.showinfo("Wrong ", "Phone Number is Exist")
        return 0
    return 1
def ScreenAddTechnician():
    frmAddTechnician = Tk()
    frmAddTechnician.geometry('400x400+500+200')
    frmAddTechnician.title('Add Technician')



    def ButtonCreateTechnician():
        if checkPhoneNumber(cbxPhoneNumberAddTechnician.get()) == 1 and checkName(cbxNameAddTechnician.get()) == 1 and checkExistPhoneNumber(cbxPhoneNumberAddTechnician.get(),TechnicianList)==1:
            CreateTechnician(cbxPhoneNumberAddTechnician.get(), cbxNameAddTechnician.get(),cbxUserNameAddTechnician.get(), cbxPasswordAddTechnician.get())
            messagebox.showinfo("Add Technician", " Add Technician  Successful")
            frmAddTechnician.destroy()

    labNameAddTechnician = ttk.Label(frmAddTechnician, text='Name:', font='arial 10').grid(row=1,  pady=10)
    cbxNameAddTechnician = ttk.Entry(frmAddTechnician)
    cbxNameAddTechnician.grid(row=1, column=1)



    labUserNameAddTechnician = ttk.Label(frmAddTechnician, text='User Name:', font='arial 10').grid(row=3,  pady=10)
    cbxUserNameAddTechnician = ttk.Entry(frmAddTechnician)
    cbxUserNameAddTechnician.grid(row=3, column=1)


    labPasswordAddTechnician = ttk.Label(frmAddTechnician, text='Password:', font='arial 10').grid(row=5,  pady=10)
    cbxPasswordAddTechnician = ttk.Entry(frmAddTechnician)
    cbxPasswordAddTechnician.grid(row=5, column=1)


    labPhoneNumberAddTechnician = ttk.Label(frmAddTechnician, text='Phone Number:', font='arial 10').grid(row=7, pady=10)
    cbxPhoneNumberAddTechnician = ttk.Entry(frmAddTechnician)
    cbxPhoneNumberAddTechnician.grid(row=7, column=1, pady=10)


    Button(frmAddTechnician, text="Add", font='times 10', command=ButtonCreateTechnician).grid(row=9,column=1)  # Button Save

    frmAddTechnician.mainloop()
def UpdateNextServiceDate():
    Date = datetime.date.today()
    DateMonth = Date.month + 6
    DateDay = Date.day
    DateYear = Date.year
    if DateMonth > 12:
        DateMonth = DateMonth - 12
        DateYear = Date.year + 1
        DateDay = Date.day
    return str(DateYear) + "-" + str(DateMonth) + "-" + str(DateDay)

def ScreenAddClient(): #new clint
    frmAddNewClient = Tk()
    frmAddNewClient.geometry('200x200+500+200')
    frmAddNewClient.title('Add New Client')
    tk.Button(frmAddNewClient, text='New Client', command=ScreenNewClient).grid(row=2,column=0,pady=20,padx=50)
    tk.Button(frmAddNewClient, text='Exists Client', command=ScreenExistsClient).grid(row=3,column=0,pady=20,padx=50)
def ScreenExistsClient():
    frmProductUpdateExistsClient = Tk()
    frmProductUpdateExistsClient.geometry('400x400+500+200')
    frmProductUpdateExistsClient.title('Exists Client')


    tk.Label(frmProductUpdateExistsClient, text="Phone Number").grid(row=4, pady=10)
    EntryPhoneNumber = tk.Entry(frmProductUpdateExistsClient)
    EntryPhoneNumber.grid(row=4, column=1)

    lst = []

    def Selected(events):
        global saveSelected
        saveSelected = lst[pro.current()]

    def checkCodeOfProduct():
        for itemName in ProductList:
            if itemName.ProductName == saveSelected:
                code = itemName.ProductCode
        return code

    for item in ProductList:
        if item.ProductName not in lst:
            lst.append(item.ProductName)

    tk.Label(frmProductUpdateExistsClient, text="Product").grid(row=5, pady=10)
    pro = ttk.Combobox(frmProductUpdateExistsClient, values=lst, width=15)
    pro.bind("<<ComboboxSelected>>", Selected)
    pro.current(0)

    pro.grid(column=1, row=5)
    text = datetime.date.today()

    tk.Label(frmProductUpdateExistsClient, text='Date:', font='arial 10').grid(row=7, pady=10)
    cbxDate = tk.Entry(frmProductUpdateExistsClient)
    cbxDate.delete(0, END)
    cbxDate.insert(0, text)
    cbxDate.grid(row=7, column=1)
    cbxDate.configure(state='readonly')

    tk.Label(frmProductUpdateExistsClient, text='Next Service Date :', font='arial 10').grid(row=8, pady=10)
    cbxNextServiceDate = tk.Entry(frmProductUpdateExistsClient)
    cbxNextServiceDate.delete(0, END)
    cbxNextServiceDate.insert(0, UpdateNextServiceDate())
    cbxNextServiceDate.grid(row=8, column=1)
    cbxNextServiceDate.configure(state='readonly')

    def click_me():
        if checkNotExistPhoneNumber(EntryPhoneNumber.get(),ClientList) == 1:
            if ProductPurchasedList == []:
                Code = 4564
            else:
                Code = int(ProductPurchasedList[len(ProductPurchasedList) - 1].PurchaseCode) + 1
            ProductPurchasedList.append(ProductPurchased(Code, checkCodeOfProduct(),EntryPhoneNumber.get(),DateToString(),UpdateNextServiceDate()))
            AddProductPurchasedListToProductPurchasedFile()
            messagebox.showinfo("Add Product", " Add New Product  Successful")
            frmProductUpdateExistsClient.destroy()

    tk.Button(frmProductUpdateExistsClient, text='Add', command=click_me).grid(row=11, column=1, sticky=tk.W, pady=10)
    frmProductUpdateExistsClient.mainloop()
def ScreenNewClient():
    frmAddClient=Tk()
    frmAddClient.geometry('400x400+500+200')
    frmAddClient.title('Add New Client')

    tk.Label(frmAddClient,text="Name").grid(row=1,pady=10)
    EntryName = tk.Entry(frmAddClient)
    EntryName.grid(row=1, column=1)

    tk.Label(frmAddClient, text="User Name").grid(row=2,pady=10)
    EntryUserName = tk.Entry(frmAddClient)
    EntryUserName.grid(row=2, column=1)

    tk.Label(frmAddClient, text="Password").grid(row=3, pady=10)
    EntryPassword = tk.Entry(frmAddClient)
    EntryPassword.grid(row=3, column=1)

    tk.Label(frmAddClient, text="Phone Number").grid(row=4, pady=10)
    EntryPhoneNumber = tk.Entry(frmAddClient)
    EntryPhoneNumber.grid(row=4, column=1)

    lst = []

    def Selected(events):
        global saveSelected
        saveSelected = lst[pro.current()]

    def checkCodeOfProduct():
        for itemName in ProductList:
            if itemName.ProductName == saveSelected:
                code = itemName.ProductCode
        return code
    for item in ProductList:
        if item.ProductName not in lst:
            lst.append(item.ProductName)

    tk.Label(frmAddClient, text="Product").grid(row=5, pady=10)
    pro = ttk.Combobox(frmAddClient, values=lst, width=15)
    if lst!=[]:
        saveSelected=lst[0]
        pro.bind("<<ComboboxSelected>>", Selected)
        pro.current(0)

    pro.grid(column=1, row=5)

    lstLocation=[]
    def SelectedLocation(events):
        global saveSelectedLocation
        saveSelectedLocation = lstLocation[proLocation.current()]

    def CondinationsForLocation():
        for item in dicLocation:
            if item == saveSelectedLocation:
                Condinations = dicLocation[item]
        print(Condinations)
        return Condinations
    for item in dicLocation:
        lstLocation.append(item)
    tk.Label(frmAddClient, text="Location").grid(row=6, pady=10)
    proLocation = ttk.Combobox(frmAddClient, values=lstLocation, width=15)
    saveSelectedLocation=lstLocation[0]
    proLocation.bind("<<ComboboxSelected>>", SelectedLocation)
    proLocation.grid(column=1, row=6)
    proLocation.current(0)
    text = datetime.date.today()

    tk.Label(frmAddClient, text='Date:', font='arial 10').grid(row=7,pady=10)
    cbxDate = tk.Entry(frmAddClient)
    cbxDate.delete(0, END)
    cbxDate.insert(0, text)
    cbxDate.grid(row=7, column=1)
    cbxDate.configure(state='readonly')

    tk.Label(frmAddClient, text='Next Service Date :', font='arial 10').grid(row=8, pady=10)
    cbxNextServiceDate = tk.Entry(frmAddClient)
    cbxNextServiceDate.delete(0, END)
    cbxNextServiceDate.insert(0, UpdateNextServiceDate())
    cbxNextServiceDate.grid(row=8, column=1)
    cbxNextServiceDate.configure(state='readonly')

    def click_me():
        if checkPhoneNumber(EntryPhoneNumber.get()) == 1 and checkName(EntryName.get()) == 1 and checkExistPhoneNumber( EntryPhoneNumber.get(),ClientList):
            AddClient(EntryUserName.get(), EntryPassword.get(), EntryPhoneNumber.get(), CondinationsForLocation(),EntryName.get(), DateToString(), UpdateNextServiceDate(), checkCodeOfProduct())
            messagebox.showinfo("Add Client", " Add Client  Successful")
            frmAddClient.destroy()

    tk.Button(frmAddClient, text='Add', command=click_me).grid(row=9, column=1, sticky=tk.W, pady=10)
    frmAddClient.mainloop()

def checkExistProdect(Prodect):
    l=[]
    for var in ProductList:
        l.append(var.ProductCode)
    if Prodect  in l:
        messagebox.showinfo("Wrong ", "Prodect is Exist")
        return 0
    else:
        return 1
def ScreenAddProdect():
    frmAddProdect = Tk()
    frmAddProdect.geometry('300x300+500+200')
    frmAddProdect.title('Add Prodect')
    def click_me():
        if(checkExistProdect(EntryProdectCode.get())==1):
            AddProducts(EntryProdectCode.get(),EntryName.get())
            messagebox.showinfo("Add Technician", " Add Prodect  Successful")
            frmAddProdect.destroy()
    ttk.Label(frmAddProdect, text='Prodect Name', font='arial 10').grid(row=1,pady=10)
    EntryName = ttk.Entry(frmAddProdect)
    EntryName.grid(row=1, column=1)
    ttk.Label(frmAddProdect, text='Prodect Code:', font='arial 10').grid(row=2, pady=10)
    EntryProdectCode = ttk.Entry(frmAddProdect)
    EntryProdectCode.grid(row=2, column=1)
    tk.Button(frmAddProdect, text='Add', command=click_me).grid(row=3, column=1, pady=10)

    frmAddProdect.mainloop()
def returnLocationByclientPhone(phoneNumber):
    for item in ClientList:
        if item.phoneNumber == phoneNumber:
            return returnLocation(item.Location)
def returnLocation(point):
    for i in dicLocation:
        if point == dicLocation[i]:
                return i
def helpFunctionForScreenTechnician(j,frmTechnician):
    ttk.Label(frmTechnician, text=' Fault Code  ').grid(row=2, column=0, pady=10)

    ttk.Label(frmTechnician, text=FaultList[j].FaultCode).grid(row=2, column=1, pady=10)

    ttk.Label(frmTechnician, text=' Product ').grid(row=3, column=0, pady=10)

    def gitNameOfProduct():
        for itemName in ProductList:
            if itemName.ProductCode == FaultList[j].ProductCode:
                name = itemName.ProductName
        return name

    ttk.Label(frmTechnician, text=gitNameOfProduct()).grid(row=3, column=1, pady=10)

    ttk.Label(frmTechnician, text=' Phone Number For Client ',).grid(row=4, column=0, pady=10)
    ttk.Label(frmTechnician, text=FaultList[j].ClientPhoneNumber).grid(row=4, column=1, pady=10)

    ttk.Label(frmTechnician, text=' Fault Date ').grid(row=5, column=0, pady=10)
    ttk.Label(frmTechnician, text=FaultList[j].FaultDate).grid(row=5, column=1, pady=10)

    ttk.Label(frmTechnician, text=' Documentation ').grid(row=6, column=0, pady=10)
    ttk.Label(frmTechnician, text=FaultList[j].Description, justify=LEFT).grid(row=6, column=1,
                                                                                                pady=10)

    ttk.Label(frmTechnician, text=' Treatment Time ').grid(row=7, column=0, pady=10)
    ttk.Label(frmTechnician, text=FaultList[j].TreatmentTime+" hour").grid(row=7, column=1, pady=10)

    ttk.Label(frmTechnician, text='City ').grid(row=8, column=0, pady=10)
    ttk.Label(frmTechnician, text=returnLocationByclientPhone(FaultList[j].ClientPhoneNumber)).grid(
        row=8, column=1, pady=10)

    ttk.Label(frmTechnician, text='Fault Type').grid(row=9, column=0, pady=10)
    def ChangeType(events):
        global saveSelectedType
        saveSelectedType = lstTypes[Type.current()]
        if FaultList[j].FaultType!=saveSelectedType:
                FaultList[j].FaultType=saveSelectedType
                FaultList[j].TreatmentTime = TreatmentTimeForFaultType(saveSelectedType)
                FaultList[j].FaultStatus = 'New Fault'
                FaultList[j].TechnicianPhoneNumber = '0'
                FaultList[j].assigningDate = "Not assigning yet"
                assigningAutomatic()


    svFaultType = StringVar()
    Type = ttk.Combobox(frmTechnician, values=lstTypes)
    Type.current(0)
    Type.delete(0, END)
    Type.insert(0,FaultList[j].FaultType)
    Type.bind('<<ComboboxSelected>>', ChangeType)
    Type.grid(row=9, column=1, pady=10)

    StatusList = ['In Progress', 'Done']

    def ChangeStatus(events):
        global saveSelectedStatus
        saveSelectedStatus = StatusList[Status.current()]
        if saveSelectedStatus=='Done':
            messagebox.showinfo("", "Good Jop :)")
            FaultList[j].FaultStatus=saveSelectedStatus
            if FaultList[j].FaultType=='Maintenance failure':
                for item in ProductPurchasedList:
                    if FaultList[j].ProductCode==item.ProductCode:
                        item.NextDateForMaintenance=UpdateNextServiceDate()


    svFaultStatus = StringVar()
    ttk.Label(frmTechnician, text=' Fault Status ').grid(column=2, row=9, pady=10)
    Status = ttk.Combobox(frmTechnician, values=StatusList)
    Status.current(0)
    Status.delete(0, END)
    Status.insert(0, FaultList[j].FaultStatus)
    #svFaultStatus.set(FaultList[j].FaultStatus)
    Status.bind("<<ComboboxSelected>>", ChangeStatus)
    Status.grid(column=3, row=9, pady=10)
k=0
def screenTechnician(user,index):
    frmTechnician = Tk()
    frmTechnician.geometry('1200x450+200+200')
    frmTechnician.title('Technician')
    Label(frmTechnician, text='Welcome' + ' ' + user.name).grid(row=1, pady=10)
    global k
    k=0
    FaultListForTechnician = []
    for i in range(len(FaultList)):
        if FaultList[i].TechnicianPhoneNumber == user.phoneNumber and FaultList[i].FaultStatus != 'Done':
            FaultListForTechnician.append(i)
    # while FaultList[FaultListForTechnician[k]].FaultStatus == 'Done':
    #     k = k + 1
    helpFunctionForScreenTechnician(FaultListForTechnician[k],frmTechnician)


    def click_close():
        frmTechnician.destroy()
        Login()
    def click_prev( frmTechnician):
        global k
        if 0<= k-1:
            k = k - 1
            # while FaultList[FaultListForTechnician[k]].FaultStatus == 'Done':
            #     k = k- 1
            if 0 <= k:
                helpFunctionForScreenTechnician(FaultListForTechnician[k], frmTechnician)
        AddFaultListToFaultFile()

    def click_Next(frmTechnician):
        global k
        if len(FaultListForTechnician) - 1 >= k + 1:
            k = k + 1
            # while FaultList[FaultListForTechnician[k]].FaultStatus == 'Done':
            #     k = k + 1
            if len(FaultListForTechnician) - 1 >= k:
                helpFunctionForScreenTechnician(FaultListForTechnician[k],frmTechnician)
        AddFaultListToFaultFile()

    Label(frmTechnician).grid(row=11,column=4, pady=10)
    if k<=len(FaultListForTechnician)-1:
         tk.Button(frmTechnician, text='next',width=10, command=lambda :click_Next(frmTechnician)).grid(row=11, column=3, pady=10,padx=10)
    else:
        tk.Button(frmTechnician, text='next').grid(row=11, column=3,pady=10,padx=10)

    if k>=0:
        tk.Button(frmTechnician, text='prev',width=10, command=lambda: click_prev(frmTechnician)).grid(row=11, column=0, pady=10,padx=10)
    else:
        tk.Button(frmTechnician, text='prev').grid(row=11, column=0,pady=10,padx=10)

    tk.Button(frmTechnician, text='View all', command=lambda:screenViewTechnician(user)).grid(row=11, column=2,pady=10,padx=10)#Amer27.11 - 1

    tk.Button(frmTechnician, text='close',width=10, command=click_close).grid(row=11, column=4,pady=10,padx=10)

    frmTechnician.mainloop()

######### Amer27.11 -2
def screenViewTechnician(user):
    frmViewTechnician = Tk()
    frmViewTechnician.geometry('1100x450+200+100')
    frmViewTechnician.title('Technician')
    Label(frmViewTechnician, text='Welcome' + ' ' + user.name, font='arial 12', fg='black').grid(row=1)

    j = 0
    for i in FaultList:
        if i.TechnicianPhoneNumber == user.phoneNumber:
            ttk.Label(frmViewTechnician, text=' Fault Code  ', font='arial 12').grid(row=2, column=0)

            ttk.Label(frmViewTechnician, text=i.FaultCode, font='arial 10').grid(row=j + 3, column=0)

            ttk.Label(frmViewTechnician, text=' Product ', font='arial 12').grid(row=2, column=2)

            def gitNameOfProduct():
                for itemName in ProductList:
                    if itemName.ProductCode == i.ProductCode:
                        name = itemName.ProductName
                return name

            ttk.Label(frmViewTechnician, text=gitNameOfProduct(), font='arial 10').grid(row=j + 3, column=2)

            ttk.Label(frmViewTechnician, text=' Phone Number For Client ', font='arial 12').grid(row=2, column=3)
            ttk.Label(frmViewTechnician, text=i.ClientPhoneNumber, font='arial 10').grid(row=j + 3, column=3)

            ttk.Label(frmViewTechnician, text='   Fault Date    ', font='arial 12').grid(row=2, column=5)
            ttk.Label(frmViewTechnician, text=i.FaultDate, font='arial 10').grid(row=j + 3, column=5)
            ttk.Label(frmViewTechnician, text='   Fault Type   ', font='arial 12').grid(row=2, column=6)

            ttk.Label(frmViewTechnician, text=i.FaultType, font='arial 12').grid(row=j + 3, column=6)

            labFaultStatus = ttk.Label(frmViewTechnician, text='   Fault Status   ', font='arial 12').grid(column=7,
                                                                                                           row=2)

            FaultStatus = ttk.Label(frmViewTechnician, text=i.FaultStatus, font='arial 12').grid(column=7,
                                                                                                 row=j + 3)

            ttk.Label(frmViewTechnician, text=' Documentation ', font='arial 12').grid(row=2, column=8)
            ttk.Label(frmViewTechnician, text=i.Description, justify=LEFT, font='arial 10').grid(row=j + 3,
                                                                                                 column=8)

            ttk.Label(frmViewTechnician, text=' Treatment Time ', font='arial 12').grid(row=2, column=9)
            ttk.Label(frmViewTechnician, text=i.TreatmentTime, font='arial 10').grid(row=j + 3, column=9)

            ttk.Label(frmViewTechnician, text='City ', font='arial 12').grid(row=2, column=10)
            ttk.Label(frmViewTechnician, text=returnLocationByclientPhone(i.ClientPhoneNumber),
                      font='arial 10').grid(row=j + 3, column=10)

            j += 1

    frmViewTechnician.mainloop()
###########


def Main():
    print("begin")
    ReadFromFiles()
    assigningDateUpdate()
    Login()
    WriteToFiles()
    print("end")
Main()

