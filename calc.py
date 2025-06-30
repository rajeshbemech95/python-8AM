# print("Welcome !!!\n Choose the option: \n 1. Add\n 2. Sub\n 3. Multiply\n 4. Devision")

# choice = input("enter your choice: ")

# n1 = int(input("Enter first value: "))
# n2 = int(input("Enter second value: "))
# if(choice == "1"):
#     print(n1+n2)
# elif(choice == "2"):
#     print(n1-n2)
# elif(choice == "4"):
#     print(n1/n2)
# else:
#     print("Choosen wrong option")
    
# import oopsEx
from oopsEx import Person as p

p = p("Python", 30)  

p.printName()
p.printAge()