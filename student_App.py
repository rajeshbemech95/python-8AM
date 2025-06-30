# import student
from student import StudentDatabase

def main():
    db = StudentDatabase()
    db.add_student(1,"Python",95)
    db.add_student(2,"Python1",94)
    db.add_student(3,"Python2",96)
    db.add_student(4,"Python3",97)
    db.add_student(5,"Python4",98)

    print("print Display all reasult ***************************************\n")
    db.display_all()

    print("print search reasult ***************************************\n")
    db.search_student(3)

    print("print delete reasult ***************************************\n")
    db.delete_student(8)

    print("print Display all reasult ***************************************\n")
    db.display_all()


# int main()
if __name__ == "__main__":
    main()
