class Employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
        
    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")
        
class Manager(Employee):
    
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size
        
    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")
  
    
class Developer(Employee):
    
    def __init__(self, name, emp_id, language):
        super().__init__(name,emp_id)
        self.language = language
        
    def show_details(self):
        super().show_details()
        print(f"Language: {self.language}")
    
mgr = Manager("Name1", "E101", 10)
dev = Developer("Dev1", "E105", "python")

mgr.show_details()
dev.show_details()