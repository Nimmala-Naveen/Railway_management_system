import mysql.connector
class routes:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Naveen@920",
            database="Railway")
    def ruoutesinsert(self,train_no,stop1,stop2,stop3,stop4):
        self.cur=self.conn.cursor()
        self.cur.execute(f"insert into routes values({train_no},'{stop1}','{stop2}','{stop3}','{stop4}')")
        self.conn.commit()
        print("Data is Inserted sucessfully")

    def train_routes_read(self):
        self.cur=self.conn.cursor()
        self.cur.execute("""select train_no,concat("stop1","--->> ","stop2","--->>",stop3"," --->> ","stop4") from routes""")
        print(self.cur.fetchall())
