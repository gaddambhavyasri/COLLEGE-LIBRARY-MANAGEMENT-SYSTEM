from tkinter import*
from tkinter import ttk
import mysql.connector   
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # =========== VARIABLE ==============
        self.member_var=StringVar()
        self.prnno_var=StringVar()
        self.title_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postid_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.days=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdate_var=StringVar()

        self.finalprice_var=StringVar()
       





        lbltitle = Label(self.root,text="Library Management System" ,bg="#c9c9c9",fg="#ff0000",bd=15,relief=RIDGE,font=("times new roman",40, "bold"),pady=3)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#c9c9c9")
        frame.place(x=0,y=100,width=1365,height=400)

        
        # ============== Data Frame Left ==========================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="#c9c9c9",fg="#ff0000",bd=12,relief=RIDGE,font=("times new roman",12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=790,height=346)
        
        lblMember=Label(DataFrameLeft,font=("arial",12, "bold"),text="Member Type:",bg="#c9c9c9")
        lblMember.grid(row=0,column=0,sticky=W)
        txtMember=Entry(DataFrameLeft,font=("arial",12, "bold"),textvariable=self.member_var,width=27)
        txtMember.grid(row=0,column=1)

        #comMember=ttk.Combobox(DataFrameLeft,state="readonly",
                                                        #font=("arial",15,"bold"),width=20)
        #comMember["value"]=("Admin Staff", "Student", "lecturer")
        #comMember.current(0)
        #comMember.grid(row=0,column=1)
        

        lblPRN_NO=Label(DataFrameLeft,bg="#c9c9c9",text="PRN NO:",font=("arial",12, "bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",12, "bold"),textvariable=self.prnno_var,width=27)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="#c9c9c9")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.title_var,width=27)
        txtTitle.grid(row=2,column=1)


        lblFristName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Frist Name:",padx=2,pady=4,bg="#c9c9c9")
        lblFristName.grid(row=3,column=0,sticky=W)
        txtFristName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=27)
        txtFristName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Last Name:",padx=2,pady=4,bg="#c9c9c9")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=27)
        txtLastName.grid(row=4,column=1)



        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=4,bg="#c9c9c9")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=27)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=4,bg="#c9c9c9")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=27)
        txtAddress2.grid(row=6,column=1)

        lblPostcode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code:",padx=2,pady=4,bg="#c9c9c9")
        lblPostcode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postid_var,width=27)
        txtPostcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=4,bg="#c9c9c9")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=27)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book ID:",padx=2,pady=4,bg="#c9c9c9")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=27)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=4,bg="#c9c9c9")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=27)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author:",padx=2,pady=4,bg="#c9c9c9")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=27)
        txtAuther.grid(row=2,column=3)

        lblDtaeBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="DateBorrowed:",padx=2,pady=4,bg="#c9c9c9")
        lblDtaeBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=27)
        txtDateBorrowed.grid(row=3,column=3,sticky=W)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="DateDue:",padx=2,pady=4,bg="#c9c9c9")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=27)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="DaysOnBook:",padx=2,pady=4,bg="#c9c9c9")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.days,width=27)
        txtDaysOnBook.grid(row=5,column=3)


        lblLateRetunFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="LateReturnFine:",padx=2,pady=4,bg="#c9c9c9")
        lblLateRetunFine.grid(row=6,column=2,sticky=W)
        txtLateRetunFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine_var,width=27)
        txtLateRetunFine.grid(row=6,column=3)

        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="DateOverDate:",padx=2,pady=4,bg="#c9c9c9")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdate_var,width=27)
        txtDateOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="ActualPrice:",padx=2,pady=4,bg="#c9c9c9")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=27)
        txtActualPrice.grid(row=8,column=3)

        
        # =========== DATA FRAME RIGHT =========================


        DataFrameRight=LabelFrame(frame,text="Book Details",bg="#c9c9c9",fg="#ff0000",bd=12,relief=RIDGE,font=("times new roman",12, "bold"))
        DataFrameRight.place(x=805,y=5,width=510,height=346)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=31,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        


        listBooks=[
            'PYTHON',
            'C language',
            'HTML',
            'CSS',
            'JAVASCRIPT',
            'R language',
            'Data Structure',
            'NodeJS',
            'C++' ,
            'PHP',
            'Reactjs',
            'java',
            'Django' ,
            'Flask',
            'Pandas', 
            'MongoDB', 
            'SQL',
            'MYSQL',
            'SQLITE3'
        ]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="PYTHON"):
                self.bookid_var.set("BKID01")
                self.booktitle_var.set("PYTHON")
                self.author_var.set("Martin C")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.835")

            elif(x=="C language"):
                self.bookid_var.set("BKID02")
                self.booktitle_var.set("C language")
                self.author_var.set("Dennis Ritchie")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.310")

            elif(x=="HTML"):
                self.bookid_var.set("BKID03")
                self.booktitle_var.set("HTML")
                self.author_var.set("Thomas Powell")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.934")

            elif(x=="CSS"):
                self.bookid_var.set("BKID04")
                self.booktitle_var.set("CSS")
                self.author_var.set("Thomas Powell")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.934")

            elif(x=="JAVASCRIPT"):
                self.bookid_var.set("BKID05")
                self.booktitle_var.set("JAVASCRIPT")
                self.author_var.set("Ockert J.du Preez")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.617")

            elif(x=="R language"):
                self.bookid_var.set("BKID06")
                self.booktitle_var.set("R language")
                self.author_var.set(" Mark Gardener")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.400")

            elif(x=="Data Structure"):
                self.bookid_var.set("BKID07")
                self.booktitle_var.set("Data Structure")
                self.author_var.set("Narasimha Karumanchi ")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.645")

            elif(x=="NodeJS"):
                self.bookid_var.set("BKID08")
                self.booktitle_var.set("NodeJS")
                self.author_var.set("Ryan Dahl")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.450")

            elif(x=="C++"):
                self.bookid_var.set("BKID09")
                self.booktitle_var.set("R language")
                self.author_var.set(" Rajesh K. Shukla")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.499")

            elif(x=="PHP"):
                self.bookid_var.set("BKID10")
                self.booktitle_var.set("PHP")
                self.author_var.set("Richard Blum")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.640")

            elif(x=="Reactjs"):
                self.bookid_var.set("BKID11")
                self.booktitle_var.set("Dinesh Rajput")
                self.author_var.set("Wayne Wolf")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.777")

            elif(x=="java"):
                self.bookid_var.set("BKID12")
                self.booktitle_var.set("java")
                self.author_var.set("D.T. Editorial Services")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.549")
            
            elif(x=="Django"):
                self.bookid_var.set("BKID13")
                self.booktitle_var.set("Django")
                self.author_var.set("Antonio Melé")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.2849")

            elif(x=="Flask"):
                self.bookid_var.set("BKID14")
                self.booktitle_var.set("Flask")
                self.author_var.set("Moaml Mohmmed")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.500")

            elif(x=="Pandas"):
                self.bookid_var.set("BKID15")
                self.booktitle_var.set("Pandas")
                self.author_var.set("Wes McKinney")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.900")

            elif(x=="MongoDB"):
                self.bookid_var.set("BKID16")
                self.booktitle_var.set("MongoDB")
                self.author_var.set("Dwight Merriman")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.500")

            elif(x=="SQL"):
                self.bookid_var.set("BKID17")
                self.booktitle_var.set("SQL")
                self.author_var.set("Richard Blum")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.640")

            elif(x=="MYSQL"):
                self.bookid_var.set("BKID18")
                self.booktitle_var.set("MYSQL")
                self.author_var.set("Ulf Michael Widenius")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.1300")

            elif(x=="SQLITE3"):
                self.bookid_var.set("BKID19")
                self.booktitle_var.set("SQLITE3")
                self.author_var.set("Dwayne Richard Hipp")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.days.set(15)
                self.latereturnfine_var.set("RS.50")
                self.dateoverdate_var.set("No")
                self.finalprice_var.set("Rs.680")


            







        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)

        # ============ BUTTONS FRAME =========================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#c9c9c9")
        Framebutton.place(x=0,y=500,width=1365,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data", font=("arial",12,"bold"),width=20,bg="#05ff05",fg="red",padx=2,pady=3)        
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data", font=("arial",12,"bold"),width=20,bg="#05ff05",fg="red",padx=2,pady=3)        
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update", font=("arial",12,"bold"),width=20,bg="#05ff05",fg="red",padx=2,pady=3)        
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete", font=("arial",12,"bold"),width=20,bg="#05ff05",fg="red",padx=2,pady=3)        
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset", font=("arial",12,"bold"),width=20,bg="#05ff05",fg="red",padx=2,pady=3)        
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit", font=("arial",12,"bold"),width=20,bg="#05ff05",fg="red",padx=2,pady=3)        
        btnAddData.grid(row=0,column=5)

        # ============ Information FRAME =========================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#c9c9c9")
        FrameDetails.place(x=0,y=570,width=1365,height=195)

        Table_frame=Frame(FrameDetails,bg="#c9c9c9",bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=2,width=1300,height=120)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname",
        "lastname","address1","address2","postid","mobile","bookid","booktitle","auther","dateborrowed",
        "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)        
 
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
 
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="Prn No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("mobile",text="Moblie")
        self.library_table.heading("bookid",text="Book Id") 
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Dateborrowed")
        self.library_table.heading("datedue",text="Datedue")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="FinalPrice")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="bhavyasri@nellore123",database="studata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prnno_var.get(),
                                                                                                                self.title_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postid_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.days.get(),
                                                                                                                self.latereturnfine_var.get(),
                                                                                                                self.dateoverdate_var.get(),
                                                                                                                self.finalprice_var.get()
                                                                                                                ))
                                                                                                            
        conn.commit()
        #self.fetch_data()
        conn.close()
        messagebox.showinfo("success","Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="bhavyasri@nellore123",database="studata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Membertype=%s,Title=%s,Firstname=%s,Lastname=%s,Address1=%s,Address2=%s,PostID=%s,Mobile=%s,BookID=%s,BookTitle=%s,Author=%s,Databorrowed=%s,Datedue=%s,Days=%s,Latereturnfine=%s,Dateoverdue=%s,Finalprice=%s where PRN_No=%s",(
                                                                                                                                                                                                                                                                       self.member_var.get(),
                                                                                                                                                                                                                                                                       self.title_var.get(),
                                                                                                                                                                                                                                                                       self.firstname_var.get(),
                                                                                                                                                                                                                                                                       self.lastname_var.get(),
                                                                                                                                                                                                                                                                       self.address1_var.get(),
                                                                                                                                                                                                                                                                       self.address2_var.get(),
                                                                                                                                                                                                                                                                       self.postid_var.get(),
                                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                                                       self.mobile_var.get(),
                                                                                                                                                                                                                                                                       self.bookid_var.get(),
                                                                                                                                                                                                                                                                       self.booktitle_var.get(),
                                                                                                                                                                                                                                                                       self.author_var.get(),
                                                                                                                                                                                                                                                                       self.dateborrowed_var.get(),
                                                                                                                                                                                                                                                                       self.datedue_var.get(),
                                                                                                                                                                                                                                                                       self.days.get(),
                                                                                                                                                                                                                                                                       self.latereturnfine_var.get(),
                                                                                                                                                                                                                                                                       self.dateoverdate_var.get(),
                                                                                                                                                                                                                                                                       self.finalprice_var.get(),
                                                                                                                                                                                                                                                                       self.prnno_var.get(),
                                                                                                                                                                                                                                                                       ))                    
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("success","member as been updated")                                                                                                                                                                                                                                                                        
        

    def fatch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="bhavyasri@nellore123",database="studata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()


        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        Cursor_row=self.library_table.focus()
        content=self.library_table.item(Cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prnno_var.set(row[1]),
        self.title_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postid_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.days.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdate_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO\t\t"+self.prnno_var.get() + "\n")
        self.txtBox.insert(END,"ID NO\t\t"+self.title_var.get() + "\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postid_var.get() + "\n")
        self.txtBox.insert(END,"Mobile\t\t"+self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Author\t\t"+self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue\t\t"+self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.days.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine\t\t"+self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDate\t\t"+self.dateoverdate_var.get() + "\n")
        self.txtBox.insert(END,"ActualPrice\t\t"+self.finalprice_var.get() + "\n")
       
    def reset(self):
        self.member_var.set(""),
        self.prnno_var.set(""),
        self.title_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postid_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.days.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdate_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prnno_var.get()=="" or self.title_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="bhavyasri@nellore123",database="studata")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prnno_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("success","Member has been deleted")


          
       





if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
