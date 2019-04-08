import tkinter as tk
from time import time,sleep
import sqlite3
from tkinter import ttk
from tkinter import *

order1:str = ""
code1:str = ""
category1:str = ""
amount1:int = 0
amount:int=0

class Restaurant:
    def __init__(self):
            global amount

            mainWindow=tk.Tk()
            mainWindow.title("The Foodie Restaurant")
            mainWindow.geometry("1000x650+400+100")

            heading1=tk.Label(mainWindow,text="Welcome to The FOODIE Restaurant!!",fg="green")
            heading1.grid()
            heading1.config(font=("Courier",20))

            heading6=tk.Label(mainWindow,text="Menu")
            heading6.grid(row=1,column=0)
            heading6.config(font=("Courier",20))

            heading4=tk.Label(mainWindow,text="OrderID    Meal                    Category        Amount")
            heading4.grid(row=2,column=0)

            heading7 = tk.Label(mainWindow, text="Appetizers")
            heading7.grid(row=3,column=0)

            headingA=tk.Label(mainWindow, text="Quantity:")
            headingA.grid(row=10,column=10,pady=(0, 10))

            # OPTIONS = [
            #     "HALF", "FULL"
            # ]
            # variable = StringVar()
            # variable.set(OPTIONS[1])
            #
            # w = OptionMenu(mainWindow, variable, *OPTIONS)
            # w.grid(row=11, column=10)
            # quantity = str(variable.get())

            v=tk.StringVar()
            tk.Radiobutton(mainWindow,text="HALF",padx=20,variable=v,value=1).grid(row=11,column=10,pady=(0, 10))
            tk.Radiobutton(mainWindow,text="FULL",padx=20,variable=v,value=2).grid(row=12,column=10)
            quantity=str(v.get())

            FA = tk.Button(mainWindow, text="1.        Chicken Wings       Appetizers       Rs 450",fg="red",width=40,command=lambda:FA())
            FA.grid(row=4,column=0,pady=(0, 10))

            def FA():
                global order1, code1, category1, amount1, amount
                order1="Chicken Wings"
                code1="FA"
                category1="Appetizers"
                amount1=450
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                print(quantity)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)


            FB = tk.Button(mainWindow, text="2.        Chicken Tikka       Appetizers       Rs 250", fg="red",width=40, command=lambda: FB())
            FB.grid(row=5,column=0,pady=(0, 10))

            def FB():
                global order1, code1, category1, amount1, amount
                order1="Chicken Tikka"
                code1="FB"
                category1="Appetizers"
                amount1=250
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if(quantity=="HALF"):
                    amount1=(amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FC = tk.Button(mainWindow, text="3.        Grilled Paneer      Appetizers       Rs 280", fg="red",width=40, command=lambda: FC())
            FC.grid(row=6,column=0,pady=(0, 10))

            def FC():
                global order1, code1, category1, amount1, amount
                order1="Grilled Paneer"
                code1="FC"
                category1="Appetizers"
                amount1=280
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FD = tk.Button(mainWindow, text="4.        Vegetable Samosa    Appetizers       Rs 50", fg="red",width=40, command=lambda: FD())
            FD.grid(row=7,column=0,pady=(0, 10))

            def FD():
                global order1, code1, category1, amount1, amount
                order1="Vegetable Samosa"
                code1="FD"
                category1="Appetizers"
                amount1=50
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FE = tk.Button(mainWindow, text="5.        Mix Veggie Soup     Appetizers       Rs 100", fg="red",width=40, command=lambda: FE())
            FE.grid(row=8,column=0,pady=(0, 10))

            def FE():
                global order1, code1, category1, amount1, amount
                order1="Mix Veggie Soup"
                code1="FE"
                category1="Appetizers"
                amount1=100
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            headingC = tk.Label(mainWindow, text="Main Course")
            headingC.grid(row=9, column=0)

            FF = tk.Button(mainWindow, text="6.        Kadahi Paneer       Main Course      Rs 275", fg="red",width=40, command=lambda: FF())
            FF.grid(row=10,column=0,pady=(0, 10))

            def FF():
                global order1, code1, category1, amount1, amount
                order1="Kadahi Paneer"
                code1="FF"
                category1="Main Course"
                amount1=275
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FG = tk.Button(mainWindow, text="7.        Butter Chicken      Main Course      Rs 280", fg="red",width=40, command=lambda: FG())
            FG.grid(row=11,column=0,pady=(0, 10))

            def FG():
                global order1, code1, category1, amount1, amount
                order1="Butter Chicken"
                code1="FG"
                category1="Main Course"
                amount1=280
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FH = tk.Button(mainWindow, text="8.        Chicken Korma       Main Course      Rs 270", fg="red",width=40, command=lambda: FH())
            FH.grid(row=12,column=0,pady=(0, 10))

            def FH():
                global order1, code1, category1, amount1, amount
                order1="Chicken Korma"
                code1="FH"
                category1="Main Course"
                amount1=270
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FI = tk.Button(mainWindow, text="9.        Special Thali       Main Course      Rs 500", fg="red",width=40, command=lambda: FI())
            FI.grid(row=13,column=0,pady=(0, 10))

            def FI():
                global order1, code1, category1, amount1, amount
                order1="Special Thali"
                code1="FI"
                category1="Main Course"
                amount1=500
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            headingH = tk.Label(mainWindow, text="Beverages")
            headingH.grid(row=14, column=0)

            FJ = tk.Button(mainWindow, text="10.        Mango Lassi         Beverages        Rs 60", fg="red",width=40, command=lambda: FJ())
            FJ.grid(row=15,column=0,pady=(0, 10))

            def FJ():
                global order1, code1, category1, amount1, amount
                order1="Mango Lassi"
                code1="FJ"
                category1="Beverages"
                amount1=60
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FK = tk.Button(mainWindow, text="11.        Kesar Lassi         Beverages        Rs 90", fg="red",width=40, command=lambda: FK())
            FK.grid(row=16,column=0,pady=(0, 10))

            def FK():
                global order1, code1, category1, amount1, amount
                order1="Kesar Lassi"
                code1="FK"
                category1="Beverages"
                amount1=90
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FL = tk.Button(mainWindow, text="12.        Shakes & Juices     Beverages        Rs 60", fg="red",width=40, command=lambda: FL())
            FL.grid(row=17,column=0,pady=(0, 10))

            def FL():
                global order1, code1, category1, amount1, amount
                order1="Shakes & Juices"
                code1="FL"
                category1="Beverages"
                amount1=60
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30
                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            FM = tk.Button(mainWindow, text="13.        Chai or Coffee      Beverages        Rs 50", fg="red",width=40, command=lambda: FM())
            FM.grid(row=18,column=0,pady=(0, 10))

            def FM():
                global order1, code1, category1, amount1, amount
                order1="Chai or Coffee"
                code1="FM"
                category1="Beverages"
                amount1=50
                Order.insert(0, order1)
                Code.insert(0, code1)
                Category.insert(0, category1)
                if (quantity == "HALF"):
                    amount1 = (amount1 / 2) + 30

                Amount.insert(0, amount1)
                amount = amount + amount1
                TAmount.insert(0, amount)

            heading2=tk.Label(mainWindow,text="Your Order::")
            heading2.grid(row=1,column=15)
            Order=tk.Entry(mainWindow,width=20)
            Order.grid(row=1,column=18,pady=(0, 10))

            heading3=tk.Label(mainWindow,text="Order ID::")
            heading3.grid(row=2,column=15,pady=(0, 10))
            Code=tk.Entry(mainWindow,width=20)
            Code.grid(row=2,column=18)

            headingM=tk.Label(mainWindow,text="Order Category::")
            headingM.grid(row=3,column=15)
            Category=tk.Entry(mainWindow, width="20")
            Category.grid(row=3,column=18)

            headingN=tk.Label(mainWindow,text="Amount:: Rs.")
            headingN.grid(row=4,column=15)
            Amount=tk.Entry(mainWindow,width=20)
            Amount.grid(row=4,column=18)


            def getvalues():
                global order1, code1, category1, amount1,amount
                getinfo(order1,code1,category1,amount1)
                Order.delete('0', tk.END)
                Code.delete('0', tk.END)
                Category.delete('0', tk.END)
                Amount.delete('0', tk.END)
                TAmount.delete('0', tk.END)


            def reset():
                Order.delete('0',tk.END)
                Code.delete('0',tk.END)
                Category.delete('0',tk.END)
                Amount.delete('0',tk.END)
                TAmount.delete('0', tk.END)


            button1=tk.Button(mainWindow,text="Submit",fg="red",command=lambda: getvalues())
            button1.grid(row=6,column=15,pady=(0, 10))

            button3=tk.Button(mainWindow, text="Reset",fg="red", command=lambda: reset())
            button3.grid(row=7,column=15,pady=(0, 10))

            button2=tk.Button(mainWindow, text="Show Values",fg="red",command=lambda: showvalues())
            button2.grid(row=8,column=15,pady=(0, 10))

            headingS = tk.Label(mainWindow, text="Total Amount:: Rs.")
            headingS.grid(row=9, column=15)
            TAmount = tk.Entry(mainWindow, width=20)
            TAmount.grid(row=9, column=18,pady=(0, 10))

            def showvalues():

                thirdWindow = tk.Tk()
                thirdWindow.title("Access Page")

                accLabel1 = tk.Label(thirdWindow, text="Access Page", fg="green")
                accLabel1.config(font=("Sylfaen", 30))
                accLabel1.grid(pady=(0, 10))

                accLabel2 = tk.Label(thirdWindow, text="Create your User ID:")
                accLabel2.grid(row=2, column=7, pady=(0, 10))

                UserID = tk.Entry(thirdWindow, width=20)
                UserID.grid(row=2, column=15, pady=(0, 10))

                accLabel3 = tk.Label(thirdWindow, text="Create your Password:")
                accLabel3.grid(row=3, column=7, pady=(0, 10))

                Password = tk.Entry(thirdWindow, width=20)
                Password.grid(row=3, column=15, pady=(0, 10))

                buttonC=tk.Button(thirdWindow,text="Already an Administrator!",command=lambda:STD())
                buttonC.grid(row=6,column=7)

                def submit():
                    connection = sqlite3.connect("restaurant1.db")  # file name
                    print("Database opened successfully")

                    TABLE_NAME = "access_table"
                    USER_ID = "user_id"
                    PASSWORD = "password"

                    connection.execute(
                        " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + USER_ID + " TEXT " + PASSWORD + " TEXT );")
                    print("TABLE CREATED SUCCESSFULLY.")

                    id = UserID.get()
                    password = Password.get()

                    connection.execute(
                        "INSERT INTO " + TABLE_NAME + " ( " + USER_ID + ", " + PASSWORD + " ) "
                        "VALUES ( '" + id + "','" + password + "' ); ")
                    connection.commit()

                SUBMIT=tk.Button(thirdWindow,text="SUBMIT", command=lambda: submit())
                SUBMIT.grid(row=4,column=7)

                SeeTheDetails=tk.Button(thirdWindow,text="See The Details", command=lambda: STD())#STD=See The Details
                SeeTheDetails.grid(row=4,column=15)

                def STD():
                    forthWindow=tk.Tk()
                    forthWindow.title("Access Page")

                    STDlabel=tk.Label(forthWindow,text="Access Page",fg="green")
                    STDlabel.config(font=("Sylfaen",30))
                    STDlabel.grid(pady=(0,10))

                    accLabel4 = tk.Label(forthWindow, text="Enter your User ID:")
                    accLabel4.grid(row=2, column=7, pady=(0, 10))

                    UserID1 = tk.Entry(forthWindow, width=20)
                    UserID1.grid(row=2, column=15, pady=(0, 10))

                    accLabel5 = tk.Label(forthWindow, text="Enter your Password:")
                    accLabel5.grid(row=3, column=7, pady=(0, 10))

                    Password1 = tk.Entry(forthWindow, width=20)
                    Password1.grid(row=3, column=15, pady=(0, 10))

                    connection = sqlite3.connect("restaurant1.db")

                    TABLE_NAME = "access_table"
                    USER_ID = "user_id"
                    PASSWORD = "password"

                    connection.execute(
                        " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + USER_ID + " TEXT, " + PASSWORD + " TEXT );")
                    print("TABLE CREATED SUCCESSFULLY.")


                    buttonB=tk.Button(forthWindow,text="Show Details",command=lambda:STD1())
                    buttonB.grid(row=5,column=7,pady=(0,10))

                    def STD1():

                        user = UserID1.get()
                        cursor = connection.execute(" SELECT * FROM " + TABLE_NAME + " where user_id='"+user+"' ;")
                        i = 0
                        print(cursor)

                        USER_ID = ''
                        PASSWORD = ''
                        for row in cursor:
                            USER_ID=row[0]
                            PASSWORD=row[1]
                            i=i+1



                        if(user==USER_ID and Password1.get()==PASSWORD):
                            showvalues1()

                        else:
                            error=tk.Label(forthWindow,text="UserID or Password is Incorrect")
                            error.grid(row=6,column=15,pady=(0,10))

                    buttonA=tk.Button(forthWindow,text="Enter New Administrator", command=lambda:showvalues())
                    buttonA.grid(row=5,column=15)



                def showvalues1():
                    connection = sqlite3.connect("restaurant.db")  # file name
                    print("Database opened successfully")

                    TABLE_NAME = "restaurant_table"
                    SERIAL_NO="serial_no"
                    ORDER_NAME = "order_name"
                    ORDER_ID = "order_id"
                    ORDER_CATEGORY = "order_category"
                    ORDER_AMOUNT = "order_amount"
                    TOTAL_AMOUNT = "total_amount"

                    connection.execute(
                        " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + SERIAL_NO + " INTEGER PRIMARY KEY AUTOINCREMENT, " + ORDER_NAME +
                        " TEXT, " + ORDER_ID + " TEXT, " + ORDER_CATEGORY + " TEXT, " + ORDER_AMOUNT + " INTEGER " + TOTAL_AMOUNT + " INTEGER " "); ")

                    secondWindow=tk.Tk()

                    secondWindow.title("Display Results")

                    appLabel=tk.Label(secondWindow,text="The FOODIE Restaurant",fg="green")
                    appLabel.config(font=("Sylfaen",30))
                    appLabel.pack()

                    tree = ttk.Treeview(secondWindow)
                    tree["columns"]=("one","two","three","four")

                    tree.heading("one",text="Order")
                    tree.heading("two",text="Order ID")
                    tree.heading("three",text="Category")
                    tree.heading("four",text="Amount")

                    cursor=connection.execute(" SELECT * FROM "+ TABLE_NAME +" ;")
                    i=0

                    for row in cursor:
                        tree.insert('',i,text=" Order "+ str(row[0]), values=(row[1], row[2], row[3], row[4]))
                        i=i+1

                    tree.pack()

            def getinfo(order2,code2,category2,amount2):

                connection = sqlite3.connect("restaurant.db")  # file name
                print("Database opened successfully")

                TABLE_NAME = "restaurant_table"
                SERIAL_NO = "serial_no"
                ORDER_NAME = "order_name"
                ORDER_ID = "order_id"
                ORDER_CATEGORY = "order_category"
                ORDER_AMOUNT = "order_amount"


                connection.execute(
                    " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + SERIAL_NO + " INTEGER PRIMARY KEY AUTOINCREMENT, " + ORDER_NAME +
                    " TEXT, " + ORDER_ID + " TEXT, " + ORDER_CATEGORY + " TEXT, " + ORDER_AMOUNT + " INTEGER ); ")
                print("TABLE CREATED SUCCESSFULLY.")

                print(order2,code2,category2,amount2)
                connection.execute(
                    "INSERT INTO " + TABLE_NAME + " ( " + ORDER_NAME + ", " + ORDER_ID + ", " + ORDER_CATEGORY + ", " +
                    ORDER_AMOUNT + " ) VALUES ( '" + order2 + "','" + code2 + "','" + category2 + "','" + str(amount2) + "' ); ")
                connection.commit()
                print("Record Added Successfully.")
                check=1
                if(check==1):
                    headingO = tk.Label(mainWindow, text="Order Placed Successfully!!")
                    headingO.grid(row=5, column=15)
                else:
                    headingO = tk.Label(mainWindow, text="Error!!")
                    headingO.grid(row=5, column=15)

                # connection.execute(
                #     " SELECT SUM( " + ORDER_AMOUNT + " ) FROM " + TABLE_NAME + "; ")
                # connection.commit()


            mainWindow.mainloop()


b = Restaurant()




