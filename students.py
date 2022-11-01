
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'studentdb')
mycursor = mydb.cursor()

while True:

    print("select an option from the menu")

    print("1 add student")

    print("2 view all students")  

    print("3 search a students")

    print("4 update the students")    

    print("5 delete a students")

    print("6 exit")

   

    choice = int(input('enter an option:'))

    if(choice==1):

        print('student enter selected')
        name = input('enter the name')

        admo = input('enter the adminnumber')

        rollno = input('enter the roll no')

        college = input('enter the college name')

        sql = 'INSERT INTO `students`(`name`, `rollnumber`, `admno`, `college`) VALUES (%s,%s,%s,%s)'

        data = (name,rollno,admo,college)

        mycursor.execute(sql , data)

        mydb.commit()

    elif(choice==2):

        print('view student')

    elif(choice==3):

        print('search student')

    elif(choice==4):

        print('update student')

    elif(choice==5):

        print('delete student')

    elif(choice==6):

        break