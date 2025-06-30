from student import StudentDatabase

db  = StudentDatabase()

while True:
    
    print("Database Menu:\n1.Add Student\n2.Display Students\n3.Serach Student with Roll No\n4.Delete Student by Roll No\n5.Exit")
    choice = input("enter your choice: ")
    
    if choice == "1":
        try:
            roll_no = int(input("Enter the Roll no"))
            name = input("Enter the Name")
            mark = float((input("Enter the Mark")))
            db.add_student(roll_no, name, mark)
        except ValueError:
            print("Provide Numeric values for Roll_no and Mark")
            
    elif choice == "2":
        db.display_all()
        
    elif choice == "3":
        try:
            rn = int(input("Enter Roll no to find"))
            db.search_student(rn)
        except ValueError:
            print("Roll no should be an inteiger")
            
    elif choice == "4":
        try:
            rn = int(input("Enter Roll no to delete"))
            db.delete_student(rn)
        except ValueError:
            print("Roll no should be an inteiger")
            
    elif choice == "5":
        print("Exiting the application")
        break
    else:
        print("Invalid option!!!!!!")