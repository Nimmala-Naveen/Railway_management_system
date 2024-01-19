# importing required modules
from train_details import details
from train_capacity import capacity
from routes import routes
from bookin import book
import numpy as np
print("************welcome to railway management system************")
print("****** for Insertin the data enter-----1---")
print("****** for Reading the data enter-----2---")
print("****** for Updating the data enter-----3---")
print("****** for Deleting the data enter-----4---")

opr=int(input("please Enter Your Operations  : "))
if opr==1:
    print("--- for inserting the data in train_details press _ 1 ")
    print("--- for inserting the data in train_capacity press _ 2 ")
    print("--- for inserting the data in Routes press _ 3 ")
    print("--- for Booking a ticket press _ 4 ")
    print("---- for Excit press _ 5")
    inopr=int(input("please select the above option : "))
    #for inserting the data in train_details
    if inopr==1:
        obj1=details()
        train_no=int(input("please enter train No : "))
        src=input("please enter the src name : ")
        dst=input("please enter the dst name : ")
        tname=input("please enter the train name : ")
        obj1.insertdetails(train_no,src,dst,tname)
    #for inserting the data in train_capacity
    if inopr==2:
        obj1=capacity()
        obj2=details()
        obj2.trainnofetch()
        train_no=int(input("please enter train No : "))
        AC_1=int(input("please enter the AC_1 name : "))
        AC_2=int(input("please enter the AC_2 name : "))
        AC_3=int(input("please enter the AC_3 name : "))
        SL=int(input("please enter the SL name : "))
        GENERAL=int(input("please enter the GENERAL name : "))
        obj1.capacityinsert(train_no,AC_1,AC_2,AC_3,SL,GENERAL)
    #for inserting the data in Routes  
    if inopr==3:
        obj1=routes()
        obj2=details()
        obj2.trainnofetchroutes()
        train_no=int(input("please enter train No : "))
        stop1=input("please enter the stop1 name : ")
        stop2=input("please enter the stop2 name : ")
        stop3=input("please enter the stop3 name : ")
        stop4=input("please enter the sto4 name : ")
        obj1.ruoutesinsert(train_no,stop1,stop2,stop3,stop4)
    #for Booking a ticket
    if inopr==4:
        source=input("From : ")
        destination=input("To : ")
        obj1=book()
        obj1.trainfetch(source,destination)
        train_no=int(input("Enter the Train Number : "))
        obj2=details()
        obj2.trainnofetch_class(train_no)
        cls=input("please Enter the class (or) Coach : ")
        p_id=np.random.randint(1000,5000000,1)[0]
        p_name=(input("Enter the Passenger Name : "))
        age=(input("Enter the Passenger Age : "))
        mobile=int(input("Enter the Passenger Mobile Number : "))
        gender=(input("Enter the Passenger Gender : "))
        obj1=book()
        obj1.addpassenger(p_id,p_name,age,mobile,gender)
        #making Transaction
        t_id=np.random.randint(1000,5000000,1)[0]
        amount=int(input("Enter the Fare : "))
        while True:
         i = np.random.randint(1, 10)
         mode = "Successfull" if i >= 5 else "Cancelled"

         if mode == "Successfull":
           print("Succesfull completed.....")
           break  # Exit the loop when mode is Cancelled
         else:
           print("Camcelled ocured")
           obj1=book()
           t_id=np.random.randint(1000,5000000,1)[0]
           p_id=int(input("enter the Passenger ID : "))
           amount=int(input("Enter the Fare : "))
           i = np.random.randint(1, 10)
           mode = "Successful" if i >= 9 else "Cancelled"
           obj1.addtransaction(t_id,p_id,amount,mode)
        # Continue the loop for further iterations
        #booking ticket
        b_id=np.random.randint(1000,5000000,1)[0]
        i=np.random.randint(0,50,1)[0]
        j=i
        seat_no=[]
        no_of_seats=int(input("enter the number of seats here : "))
        while j<i+no_of_seats:
         seat_no.append(j)
         j+=1
        obj1.bookticket(b_id,p_id,cls,seat_no,t_id,source,destination,train_no,no_of_seats)

    if inopr==5:
        print("YOUR EXICT")


if opr==2:
    print("--- for Reading  the data in Book_tickets  press _ 1 ")
    print("--- for Reading the data in train_details press _ 2 ")
    print("--- for Reading the data in Routes press _ 3 ")
    print("--- for Reading the data in train_capacity press _ 4 ")
    print("--- for EXICT press _ 5 ")
    inopr1=int(input("please select the above option : "))
    if inopr1==1:
        obj1=book()
        p_id=int(input("Enter the Passenger ID Nummber :  "))
        mobile=int(input("Enter the passenger NUmber : "))
        obj1.bookticketread(p_id,mobile)
    if inopr1==2:
        source=input("From : ")
        destination=input("To : ")
        obj1=book()
        obj1.trainfetch(source,destination)
        inopr3=int(input("please select the above option : "))
        print("--- for Train_details press _ 1 ")
        print("--- for Excit press_2 ")
        if inopr3==1:
            obj1=details()
            obj1.train_details_read()
        else:
            inopr3==2
            print("YOUR EXCIT....")
    if inopr1==3:
        obj1=routes()
        obj1.train_routes_read()
    
    if inopr1==4:
        obj1=capacity()
        obj1.train_capacity_read()

    if  inopr1==5:
        print("YOUR EXCIT.....")

    

if opr==3:
    print("--- for Update the Passengers Name press _ 1 ")
    print("--- for Update the Passengers Age press _ 2 ")
    print("--- for Update the Passengers Number press _ 3 ")
    print("--- for Update the Passengers Gender press _ 4 ")
    print("--- for Excit press_5 ")
    inopr2=int(input("please select the above option : "))
    if inopr2==1:
        obj1=book()
        p_name=str(input("Enter the Passengers name : "))
        p_id=int(input("Enter the Passenger ID Nummber :  "))
        obj1.passenger_name(p_name,p_id)
    
    if inopr2==2:
        obj1=book()
        age=int(input("Enter the Passengers name : "))
        p_id=int(input("Enter the Passenger ID Nummber :  "))
        obj1.passenger_age(age,p_id)

    if inopr2==3:
        obj1=book()
        mobile=int(input("Enter the Passengers Number : "))
        p_id=int(input("Enter the Passenger ID Nummber :  "))
        obj1.passenger_mobile(mobile,p_id)

    if inopr2==4:
        obj1=book()
        gender=str(input("Enter the Passengers gender : "))
        p_id=int(input("Enter the Passenger ID Nummber :  "))
        obj1.passenger_gender(gender,p_id)

    if  inopr2==5:
        print("Your EXCIT..... ")

if opr==4:
    obj1=book()
    p_id=int(input("Enter the Passenger Number"))
    obj1.passenger_delete(p_id)
    print("sucesfully deleted")









