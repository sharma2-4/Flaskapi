from sqlite3 import connect, Row




class db:

    con = connect("db.sqlite", check_same_thread = False)
    con.row_factory = Row

    def execute(query):
        try :
            db.con.execute(query)
            db.con.commit()
        except Exception as e:
            return e

    def fetchOne(query):
        cursor = db.con.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if result: return dict(result)

    def fetchAll(query):
        cursor = db.con.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        if data: return db.get_json(data)


    def get_json(obj):
        return [dict(i) for i in obj]



class Students:
    
    __table__ = "students"

    __schema__ = "create table students (register_number integer primary key, name varchar not null, department varchar not null, attendance_percentage real, cgpa real)"


    def Verify(reg_no, dpt):
        stdnt = Students.GetStudent(reg_no)
        if stdnt:
            return dpt == stdnt["department"]


    def insert(reg_no, name, dpt, atdnce = None, cgpa = None):
        query = "insert into students values ({},'{}','{}','{}','{}')".format(reg_no, name, dpt, atdnce, cgpa)
        return db.execute(query)

    def GetStudent(reg_no):
        query = "select * from students where register_number = '{}'".format(reg_no)
        return db.fetchOne(query)

    def GetAllStudents():
        query = "select * from students"

        return db.fetchAll(query)



    


