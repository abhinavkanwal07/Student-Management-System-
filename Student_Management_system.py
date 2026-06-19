# This is the code of Student Management System . The summary of this code is that you have to select your University and then login . 
# after that some opeartions are their you can use them and can access student informations  
import time   

class University: 
    def __init__(self):
        print('''Choose Your University 
                1. JIIT NOIDA 
                2. JUIT SOLAN 
                3. JUET GUNA 
                4. JAYPEE ANOOPSHAHR 
                ''')
        Uni_no = int(input("Enter Your University Number from above list (Univeristy Number is Serial Number like 1. for JIIT NOIDA and so on ) Please type only integers  : "))
        

        if Uni_no == 1 : 
            print("Welcome To JIIT NOIDA ")
        elif Uni_no == 2 : 
            print("Welcome to JUIT SOLAN ")
        elif Uni_no == 3: 
            print("Welcome to JUET GUNA")
        elif Uni_no == 4 : 
            print("Welcome to JAYPEE ANOOPSHAHR")
        else : 
            print("Invalid operation ") 
            exit() 
        
            
class Login: 
    def login(self):
        username = "Abhinav"
        password = "123456"
        time.sleep(2)
        print('''Attention ! Attention ! Attention ! 
                 You Only have 3 chances to login !!
                 If you can't login within these chances . You have to wait for a while .
                 This is for security purposes . So please Cooperate and Write correct credentials ''')
        for i in range(1,5):
           if i < 4 : 
            Attempt = i
            print("Attempt : " , i )
            login_id = input("Enter your Username : ").strip() 
            key = input("Enter your password : ").strip() 
            if login_id == username and key == password :  
               print("Login successfully !! ")
               return True 
            elif login_id == username and key != password: 
                print("Incorrect Password") 
            elif login_id != password and key == password: 
               print("Incorrect Username")
            else :
               print("Incorrect Credentials")
           else : 
               print('''Your Have used your 3 Attempts. 
Now Login after some time  ''')
               exit() 
class Student_Details(Login,University): 
    def student_info(self,name, Roll_no , Age , Year , Batch , Course , Branch , DOB , DOJ , DOC , ):
        self.name = name 
        self.Roll_no = Roll_no 
        self.Age = Age 
        self.Year = Year 
        self.Batch = Batch 
        self.Course = Course 
        self.Branch = Branch
        self.DOB = DOB
        self.DOJ = DOJ 
        self.DOC = DOC 
        time.sleep(2)
        print(f'''Hey {self.name}.  Welcome!! 
How Can I help You 
1. Check Your Information  
2. Check Your Attendance 
3. Check Your Academics Report
4. Check Your Subjects Information 
5. Check Your Examination Schedule 
6. Check Your Fees Payment Report 
7. Exit''')
    def selection(self): 
        i = int(input("Select Serial Number from above information (like to check your information type 1 and so on  ) : "))
        if i == 1 :
            self.print_student_info() 
        elif i == 2 : 
            self.check_attendance() 
        elif i == 3 : 
            self.academic_report() 
        elif i == 4 : 
            self.subject_information() 
        elif i == 5 : 
            self.examination_schedule()
        elif i == 6 : 
            self.fees_report() 
        elif i == 7 :
            print("Exited Successfully")
            exit() 
        else : 
            print("Invalid Opeartion")
    
    def print_student_info(self): 
        print(f'''!!! STUDENT DETAILS !!!
        Name : {self.name}
        Roll Number : {self.Roll_no}
        Age : {self.Age}
        DOB : {self.DOB}
        Year : {self.Year}
        Course : {self.Course}
        Branch : {self.Branch}
        Batch : {self.Batch}
        Date of Joining : {self.DOJ}
        Date of Completion : {self.DOC}
''')    
        self.selection()
    def check_attendance(self): 
        with open ("Attendance.txt", "r") as f : 
            attendance = f.read() 
            print(attendance)
            self.selection()
    def academic_report(self):
        with open ("Academic_report.txt" , "r") as f : 
            academic = f.read() 
            print(academic)
        self.selection()
    def subject_information(self): 
        with open ("Subjects.txt" , "r") as f : 
            Subject = f.read() 
            print(Subject)
        self.selection()
    def examination_schedule(self): 
        with open ("Exams_Schedule.txt" ,"r") as f : 
            Exams = f.read() 
            print(Exams)
        self.selection()
    def fees_report(self):
        with open ("Fee_report.txt" , "r") as f : 
            Fee = f.read() 
            print(Fee)
        self.selection()
    def Greet(self):
        print("Thank YOU !! We hope you have got your Information  . ")
        print("See you soon ")
    
S1 = Student_Details()
S1.login() 
S1.student_info("Abhinav Kanwal" , 251020004 , 19,"2nd" , "25BT19" , "B.Tech" ,"CSE" , "11/04/2007" , "JULY 2025" , "MAY 2029")
S1.selection()  
S1.Greet()     
