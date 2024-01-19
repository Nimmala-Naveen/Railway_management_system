import mysql.connector
class book:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naveen@920",
            database="Railway")
        
    def trainfetch(self,source,destination):
        self.cur=self.conn.cursor()
        self.cur.execute(f"""select routes.train_no,source,stop1,stop2,stop3,stop4,destination from 
                         routes inner join train_details on routes.train_no=train_details.train_no 
                         where source='{source}'or stop1='{source}'or stop2='{source}' or stop3='{source}' or stop4='{source}'""")
        dt=self.cur.fetchall()
        try:
            tr=[]
            for i in dt:
                for j in i[i.index(source)+1:]:
                    if j == destination:
                      tr.append(i)
        except:
            pass
        print(tr)
    
    def addpassenger(self,p_id,P_name,age,mobile,gender):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into passengers values({p_id},'{P_name}','{age}','{mobile}','{gender}')")
        self.conn.commit()
        print("passenger added sucessfully")
    def addtransaction(self,t_id,p_id,amount,mode):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into transactions values({t_id},'{p_id}','{amount}','{mode}')")
        self.conn.commit()
        print("your status :",mode)
        print("transaction  sucessfully")

    def bookticket(self,b_id,p_id,cls,seat_no,t_id,source,destination,train_no,no_of_seats):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into book_tickets values('{b_id}','{p_id}','{cls}','{seat_no}','{t_id}','{source}','{destination}','{train_no}','{no_of_seats}')")
        self.conn.commit()
        print("Ticket----->  sucessfully")
        print("**********************************")
        print("passenger ID : ",p_id)
        print("Seat NUmber : ",seat_no)
        print("Booking ID : ",b_id)
        print("Class or couch : ",cls)
        print("Source  :  ",source)
        print("Destination : ",destination)
        print("Train Number Here ",train_no)
        print("Your Transaction id : ",t_id)

    def bookticketread(self,p_id,mobile):
        self.cur=self.conn.cursor()
        self.cur.execute(f"""select * from passengers inner join book_tickets
                             on passengers.p_id = book_tickets.p_id 
                             inner join transactions on book_tickets.p_id=transactions.P_id
                             where passengers.p_id ='{p_id}' and mo_num='{mobile}'""")
        dt2 = self.cur.fetchall()

        if dt2:
            columns = [i[0] for i in self.cur.description]
            for j in dt2:
                row_dict = dict(zip(columns, j))
                print(row_dict)
        else:
            print("No records found.")

    def passenger_name(self,p_name,p_id):
      while True:
        try:
            self.cur=self.conn.cursor()
            self.cur.execute(f"""update  passengers set p_name='{p_name}' where p_id='{p_id}'""")
            affected_rows=self.cur.rowcount
            self.conn.commit()
            if affected_rows>0:
             print("Data Sucesfully Updated....")
             break # Exit the loop if data is successfully updated
            else:
                print(f"No matching records found for Passenger ID = {p_id} and passenger_ Name='{p_name}' . No data updated.")
                # agian Enter the user until condition satisfeid
                # Prompt user for new input to continue the loop
                p_name=str(input("Enter the Passengers Age : "))
                p_id = int(input("Enter a valid Passenger ID: "))
        except mysql.connector.Error as err:
            print(f"Error: {err}")  


    def passenger_age(self,age,p_id):
      while True:
        try:
            self.cur=self.conn.cursor()
            self.cur.execute(f"""update  passengers set age='{age}' where p_id='{p_id}'""")
            affected_rows=self.cur.rowcount
            self.conn.commit()
            if affected_rows>0:
             print("Data Sucesfully Updated....")
             break # Exit the loop if data is successfully updated
            else:
                print(f"No matching records found for Passenger ID = {p_id} and passenger_ age='{age}' . No data updated.")
                # agian Enter the user until condition satisfeid
                # Prompt user for new input to continue the loop
                age=int(input("Enter the Passengers Age : "))
                p_id = int(input("Enter a valid Passenger ID: "))
        except mysql.connector.Error as err:
            print(f"Error: {err}")  


    def passenger_mobile(self,mobile,p_id):
      while True:
        try:
            self.cur=self.conn.cursor()
            self.cur.execute(f"""update  passengers set mo_num='{mobile}' where p_id='{p_id}'""")
            affected_rows=self.cur.rowcount
            self.conn.commit()
            if affected_rows>0:
              print("Data Sucesfully Updated....")
              break # Exit the loop if data is successfully updated
            else:
                print(f"No matching records found for Passenger ID = {p_id} and mobile_number='{mobile}' . No data updated.")
                # agian Enter the user until condition satisfeid
                # Prompt user for new input to continue the loop
                mobile=int(input("Enter the Passengers mobile  Number : "))
                p_id = int(input("Enter a valid Passenger ID: "))
        except mysql.connector.Error as err:
            print(f"Error: {err}")     

    def passenger_gender(self, gender, p_id):
      while True:
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(f"""UPDATE passengers SET gender='{gender}' WHERE p_id='{p_id}'""")
            affected_rows = self.cur.rowcount
            self.conn.commit()
            if affected_rows > 0:
                print("Data Successfully Updated.....")
                break  # Exit the loop if data is successfully updated
            else:
                print(f"No matching records found for Passenger ID = {p_id} and gender='{gender}' . No data updated.")
                # agian Enter the user until condition satisfeid
                # Prompt user for new input to continue the loop
                gender=str(input("Enter the Passengers gender : "))
                p_id = int(input("Enter a valid Passenger ID: "))
                
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def passenger_delete(self, p_id):
     try:
        self.cur = self.conn.cursor()

        # Delete from 'book_tickets' table
        self.cur.execute(f"""delete from book_tickets where p_id='{p_id}'""")

        # Delete from 'passengers' table
        self.cur.execute(f"""delete  from passengers where p_id='{p_id}'""")

        # Delete from 'transactions' table
        self.cur.execute(f"""delete from transactions where p_id='{p_id}'""")

        self.conn.commit()
        print("Data Successfully Deleted")

     except mysql.connector.Error as err:
        print(f"Error: {err}")                    

















