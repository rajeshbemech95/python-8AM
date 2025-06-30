class Student:
    
    def __init__(self,roll_no, name, mark):
        self.roll_no = roll_no
        self.name = name
        self.mark = mark
        
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Mark:,{self.mark}")
        
        
class StudentDatabase:
    def __init__(self):
        self.student = []
        
    def add_student(self,roll_no, name, mark):
        self.student.append(Student(roll_no, name, mark))
        print("Student data added")

    def display_all(self):
        if not self.student:
            print("No data available")
        else:
            for s in  self.student:
                # print(s)
                s.display()
            
    def search_student(self, rn):
        found = False
        for s in self.student:
            if s.roll_no == rn:
                s.display()
                found = True
                break
        if not found:
            print("Given roll_no not found")
            
            
                
    def delete_student(self,rn):
        found = False
        for s in self.student:
            if s.roll_no == rn:
                self.student.remove(s)
                print("Studen data deleted")
                found = True
                break
        if not found:
            print("Given roll_no not found")


# Student(3,"python",99)
# db = StudentDatabase()
# db.add_student(1,"Python",95)
# db.add_student(2,"Python1",94)
# db.add_student(3,"Python2",96)
# db.add_student(4,"Python3",97)
# db.add_student(5,"Python4",98)

# print("print Display all reasult ***************************************\n")
# db.display_all()

# print("print search reasult ***************************************\n")
# db.search_student(3)

# print("print delete reasult ***************************************\n")
# db.delete_student(8)

# print("print Display all reasult ***************************************\n")
# db.display_all()
