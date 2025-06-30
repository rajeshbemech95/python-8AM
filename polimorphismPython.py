# import inheritancePython as i 
# myClass = i.Employee("name",10)
# myClass.name



class Payment:
    def pay(self, amount):
        print("Amount Paid ", amount)
        
class CreaditCard(Payment):
    def pay(self, amount):
        print(f"Amount paid {amount} using credit card")
        
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Amount paid {amount} using cash")
        
class UPI(Payment):
    def pay(self, amount):
        print(f"Amount paid {amount} using UPI")
        
# payment = UPI()
# payment.pay(500)

# payment = CashPayment()
# payment.pay(500)

def process_payment(method,amount):
    method.pay(amount)
    
process_payment(CreaditCard(),500)

process_payment(UPI(),1000)
process_payment(CashPayment(),1500)