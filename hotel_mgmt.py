from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime


class Hotel:

    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=14, width=1350, height=550, padx=20, relief=RIDGE, bg="cadet blue")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=10, width=450, height=550, padx=2, relief=RIDGE, bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10, width=820, height=550, padx=2, relief=RIDGE, bg="cadet blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=20, relief=RIDGE, bg="powder blue")
        BottomFrame.pack(side=BOTTOM)
#----------------------------------------------Functions----------------------------------------------------------------------------
#EXIT FUNCTION
        def exit():
            exit = tkinter.messagebox.askyesnocancel("Hotel Management System", "Are You Sure to Exit?")
            if exit > 0:
                root.destroy()
                return
#RECIEPT FUNCTION
        def recipt():
            self.textdetails.insert(END,"-------------------CUSTOMER DETAILS---------------------"+"\n"+"Customer ID = "+
                                    CustomerId.get()+"\n"+"First Name= " + FirstName.get()+"\n"+ "Sur Name = " +SurName.get()+"\n"+"Address = " +Address.get()
                                  +"\n"+"Post Code = " + PostCode.get()+"\n"+ "Mobile = " + MobileNo.get()+"\n"+ "Email = "+
                                   Email.get()+"\n"+"ID Proof = "+ IdProof.get() +"\n"+"Nationality = " + Nationality.get()+"\n"+"Room No = "+ RoomNo.get()+"\n"+
                                  "Room Type = " + RoomType.get() +"\n"+"Room Extention Phone = " + RoomExt.get() + "\n" +"Number of Days = " + NoDays.get()
                                  +"\n"+ "Tax Paid = " + TaxPaid.get() +"\n"+"Sub Total = "+ SubTotal.get()+"\n"+
                                  "Total Cost = " + TotalCost.get()+"\n"+"Check-In = " + CheckIn.get() +"\n"+"Check-Out = " + CheckOut.get()+"\n")
#RESET FUNCTION
        def reset():
            CustomerId.set("")
            FirstName.set("")
            SurName.set("")
            Address.set("")
            PostCode.set("")
            MobileNo.set("")
            Email.set("")
            IdProof.set("")
            Nationality.set("")
            RoomNo.set("")
            RoomType.set("")
            RoomExt.set("")
            NoDays.set("")
            TaxPaid.set("")
            SubTotal.set("")
            TotalCost.set("")
            CheckIn.set("")
            CheckOut.set("")
            self.textdetails.delete("1.0", END)

#Total cost and date

        def totalfunc():
            indate = CheckIn.get()
            outdate = CheckOut.get()
            indate =datetime.strptime(indate, "%d/%m/%Y")
            outdate=datetime.strptime(outdate,"%d/%m/%Y")
            NoDays.set(abs(outdate-indate).days)

            if RoomType.get() == "single":
                singleprice = float(input("Enter Single Room Cost:"))
                f1 = singleprice
                f2 = float(NoDays.get())
                f3 = float(f1*f2)
                TP = (f3 / 100) * 18
                ST = f3
                TC = ST + TP
                TaxPaid.set(TP)
                SubTotal.set(ST)
                TotalCost.set(TC)

            if RoomType.get() == "double":
                doubleprice = float(input("Enter Double Room Cost:"))
                f1 = doubleprice
                f2 = float(NoDays.get())
                f3 = float(f1*f2)
                TP = (f3 / 100) * 18
                ST = f3
                TC = ST + TP
                TaxPaid.set(TP)
                SubTotal.set(ST)
                TotalCost.set(TC)

            if RoomType.get() == "family":
                familyprice = float(input("Enter Family Room Cost:"))
                f1 = familyprice
                f2 = float(NoDays.get())
                f3 = float(f1*f2)
                TP = (f3 / 100) * 18
                ST = f3
                TC = ST + TP
                TaxPaid.set(TP)
                SubTotal.set(ST)
                TotalCost.set(TC)

#TEXT-VARIABLE INITIALISATION
        CustomerId = StringVar()
        FirstName = StringVar()
        SurName = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        MobileNo = StringVar()
        Email = StringVar()
        IdProof = StringVar()
        Nationality = StringVar()
        RoomNo = StringVar()
        RoomType = StringVar()
        RoomExt = StringVar()
        NoDays = StringVar()
        TaxPaid = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()
        CheckIn = StringVar()
        CheckOut = StringVar()

#------------------------------------------Widgets----------------------------------------------------------------

#CUSTOMER ID
        self.custidlabel = Label(LeftFrame, font = ('arial', 12, 'bold'), text="Customer Id", padx=2, bg="powder blue")
        self.custidlabel.grid(row=0, column = 0, sticky=W)
        self.custidtxt = Entry(LeftFrame, width = 20, textvariable = CustomerId)
        self.custidtxt.grid(row=0, column = 1)

# FIRST NAME
        self.firstnamelabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="First Name", padx=2, pady=10, bg="powder blue")
        self.firstnamelabel.grid(row=1, column=0, sticky=W)
        self.firstnametxt = Entry(LeftFrame, width=20, textvariable=FirstName)
        self.firstnametxt.grid(row=1, column=1)

#SUR NAME
        self.surnamelabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Sur Name", padx=2, pady=10, bg="powder blue")
        self.surnamelabel.grid(row= 2, column=0, sticky=W)
        self.surnametxt = Entry(LeftFrame, width=20, textvariable=SurName)
        self.surnametxt.grid(row=2, column=1)

#ADDRESS
        self.addresslabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Address", padx=2, pady=10,  bg="powder blue")
        self.addresslabel.grid(row=3, column=0, sticky=W)
        self.addresstxt = Entry(LeftFrame, width=20, textvariable=Address)
        self.addresstxt.grid(row=3, column=1)

#PostCode
        self.postcodelabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Post Code", padx=2, pady=10,  bg="powder blue")
        self.postcodelabel.grid(row=4, column=0, sticky=W)
        self.postcodetxt = Entry(LeftFrame, width=20, textvariable=PostCode)
        self.postcodetxt.grid(row=4, column=1)
#phone
        self.phonelabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Mobile", padx=2, pady=10,  bg="powder blue")
        self.phonelabel.grid(row=5, column=0, sticky=W)
        self.phonetxt = Entry(LeftFrame, width=20, textvariable=MobileNo)
        self.phonetxt.grid(row=5, column=1)
#Email
        self.emaillabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Email", padx=2, pady=10,  bg="powder blue")
        self.emaillabel.grid(row=6, column=0, sticky=W)
        self.emailtxt = Entry(LeftFrame, width=20, textvariable=Email)
        self.emailtxt.grid(row=6, column=1)
#Identity
        self.identitylabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="ID Proof", padx=2, pady=10,  bg="powder blue")
        self.identitylabel.grid(row=7, column=0, sticky=W)
        self.identitytxt = ttk.Combobox(LeftFrame, width=20, textvariable=IdProof, state='readonly')
        self.identitytxt.grid(row=7, column=1, padx = 3, pady= 10)
        self.identitytxt['value']=('','Passport', 'Driving Licence', "voter Id", "Aadhar Card")
        self.identitytxt.current(0)

#nationality
        self.nationalitylabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Nationality", padx=2, pady=10,  bg="powder blue")
        self.nationalitylabel.grid(row=8, column=0, sticky=W)
        self.nationalitytxt =ttk.Combobox(LeftFrame, width=20, textvariable=Nationality, state='readonly')
        self.nationalitytxt['value'] = ('', 'Indian', 'British', 'American', 'Pakistani','Russian', 'Australian', 'Canadian', 'European', 'African')
        self.nationalitytxt.current(0)
        self.nationalitytxt.grid(row=8, column=1, padx=3, pady=10)

#CHECK-IN DATE
        self.checkinlabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Check-In", padx=2, pady=10,
                                   bg="powder blue")
        self.checkinlabel.grid(row=9, column=0, sticky=W)
        self.checkintxt = Entry(LeftFrame, width=20, textvariable=CheckIn)
        self.checkintxt.grid(row=9, column=1)

#CHECK-OUT DATE
        self.checkoutlabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Check-Out", padx=2, pady=10,
                                   bg="powder blue")
        self.checkoutlabel.grid(row=10, column=0, sticky=W)
        self.checkouttxt = Entry(LeftFrame, width=20, textvariable=CheckOut)
        self.checkouttxt.grid(row=10, column=1)
#room no
        self.roomnolabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Room No", padx=2, pady=10,  bg="powder blue")
        self.roomnolabel.grid(row=11, column=0, sticky=W)
        self.roomnotxt = Entry(LeftFrame, width=20, textvariable=RoomNo)
        self.roomnotxt.grid(row=11, column=1)
#room type
        self.roomtypelabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Room Type", padx=2, pady=10,  bg="powder blue")
        self.roomtypelabel.grid(row=12, column=0, sticky=W)
        self.roomtypetxt = ttk.Combobox(LeftFrame, width=20, textvariable=RoomType,state="readonly")
        self.roomtypetxt['value']= (" ", "single", "double", "family")
        self.roomtypetxt.current(0)
        self.roomtypetxt.grid(row=12, column=1)
#room extention
        self.extentionlabel = Label(LeftFrame, font=('arial', 12, 'bold'), text="Room Ext", padx=2, pady=10,  bg="powder blue")
        self.extentionlabel.grid(row=13, column=0, sticky=W)
        self.extentiontxt = Entry(LeftFrame, width=20, textvariable=RoomExt)
        self.extentiontxt.grid(row=13, column=1)


#------------------------------------------Recipt---------------------------------------------------------------------------------
#CUSTOMER LABEL
        self.detailsofcustomer = Label(RightFrame, pady=10, bg="cadet blue", font=('arial',10,'bold'),
                                       text= "CUSTOMER DETAILS")
        self.detailsofcustomer.grid(row=0, column=0, columnspan=17)

#CUSTOMER DETAILS DISPLAY
        self.textdetails = Text(RightFrame, font=('arial',10,'bold'), height = 15, width = 120, bd=10)
        self.textdetails.grid(row=1, column=0, columnspan=2, padx=2, pady=5)



#--------------------------------------------Reciept-------------------------------------------------------------------------------
#number of days
        self.numberofdays = Label(RightFrame, font=("arial", 14, "bold"), text = 'No of Days', bg="cadet blue", fg="black")
        self.numberofdays.grid(row=2, column=0, sticky=W)
        self.numberofdaystxt = Entry(RightFrame, font=("arial", 14, "bold"), textvariable = NoDays, bg="white", bd=7,width=67,justify=LEFT)
        self.numberofdaystxt.grid(row = 2, column = 1)
#tax paid
        self.taxpaid = Label(RightFrame, font=("arial", 14, "bold"), text = 'Tax', bg="cadet blue", fg="black")
        self.taxpaid.grid(row=3, column=0, sticky=W)
        self.taxpaidtxt = Entry(RightFrame, font=("arial", 14, "bold"), textvariable = TaxPaid, bg="white", bd=7,width=67,justify=LEFT)
        self.taxpaidtxt.grid(row = 3, column = 1)
#subtotal
        self.subtotal = Label(RightFrame, font=("arial", 14, "bold"), text = 'Sub Total', bg="cadet blue", fg="black")
        self.subtotal.grid(row=4, column=0, sticky=W)
        self.subtotaltxt = Entry(RightFrame, font=("arial", 14, "bold"), textvariable = SubTotal, bg="white", bd=7,width=67,justify=LEFT)
        self.subtotaltxt.grid(row = 4, column = 1)
#total amount
        self.totalamount = Label(RightFrame, font=("arial", 14, "bold"), text = 'Total Cost', bg="cadet blue", fg="black")
        self.totalamount.grid(row=5, column=0, sticky=W)
        self.totalamounttxt = Entry(RightFrame, font=("arial", 14, "bold"), textvariable = TotalCost, bg="white", bd=7,width=67,justify=LEFT)
        self.totalamounttxt.grid(row = 5, column = 1)

#----------------------------------------------BUTTON-----------------------------------------------------------------------------

#TOTAL BUTTON

        self.totalbutton = Button(BottomFrame, padx=16, pady=1,bd=4, text="Total", font=("arial",10,"bold"), width=30, height=2,
                                  bg="powder blue", fg="black",command=totalfunc).grid(row=0,column=4, padx=4)
#RECIEPT BUTTON
        self.reciptbutton = Button(BottomFrame, padx=16, pady=1, bd=4, text="Reciept", font=("arial", 10, "bold"), width=30, height=2,
                                  bg="powder blue", fg="black",command=recipt ).grid(row=0, column=5, padx=5)
#RESET BUTTON
        self.resetbutton = Button(BottomFrame, padx=16, pady=1, bd=4, text="Reset", font=("arial", 10, "bold"), width=30, height=2,
                                  bg="powder blue", fg="black", command=reset ).grid(row=0, column=6, padx=5)
#EXIT BUTTON
        self.exitbutton = Button(BottomFrame, padx=16, pady=1, bd=4, text="Exit", font=("arial", 10, "bold"), width=30, height=2,
                                  bg="powder blue", fg="black", command=exit).grid(row=0, column=7, padx=5)


if __name__=='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()

