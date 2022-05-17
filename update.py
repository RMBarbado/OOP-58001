import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Ralph Mikhail\OneDrive\Documents\Database1.accdb;')
    print("Connected to a Database")

    Fullname = "Ralph Mikhail B. Barbado"
    Assignment = 90
    Laboratory = 100
    Quiz = 95
    Exam = 100
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ?, Assignment = ?, Laboratory = ?, Quiz = ?, Exam = ? WHERE id=?', (Fullname, Assignment, Laboratory, Quiz, Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
