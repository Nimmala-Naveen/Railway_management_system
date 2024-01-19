import mysql.connector
class capacity:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naveen@920",
            database="Railway")
    def capacityinsert(self,train_no,AC_1,AC_2,AC_3,SL,GENERAL):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into train_capacity values({train_no},'{AC_1}','{AC_2}','{AC_3}','{SL}','{GENERAL}')")
        self.conn.commit()
        print("Data is Inserted sucessfully")

    def train_capacity_read(self):
        self.cur=self.conn.cursor()
        self.cur.execute(f"""select * from train_capacity""")
        self.cur.fetchall()

    