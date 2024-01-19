import mysql.connector
class details:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naveen@920",
            database="Railway")
    def insertdetails(self,train_no,src,dst,tname):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into train_details values({train_no},'{src}','{dst}','{tname}')")
        self.conn.commit()
        print("Data is Inserted sucessfully")
    def trainnofetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute("""select train_details.train_no from train_details left join 
                         train_capacity on train_details.train_no=train_capacity.train_no 
                         where ac_1 is null""")
        print(self.cur.fetchall())
    def trainnofetchroutes(self):
        self.cur=self.conn.cursor()
        self.cur.execute("""select train_details.train_no,source,destination from train_details 
                         left join routes on train_details.train_no=routes.train_no 
                         where stop1 is null""")
        print(self.cur.fetchall())

    def train_details_read(self):
        self.cur=self.conn.cursor()
        self.cur.execute("""select train_no,concat("source"," ----->> ","destination"),train_name from train_details""")
        print(self.cur.fetchall())

    def trainnofetch_class(self,train_no):
        self.cur=self.conn.cursor()
        self.cur.execute(f"""select * from train_capacity where train_no='{train_no}'""")
        dt2 = self.cur.fetchall()

        if dt2:
            columns = [i[0] for i in self.cur.description]
            for j in dt2:
                row_dict = dict(zip(columns, j))
                print(row_dict)
        else:
            print("No records found.")


    

