import os
import time
import threading

def printNum(a):
    
    for i in range(1000):
        print(i)
        time.sleep(1)
        
def alpha():
    ls = "qwertyuiopasdfghjkl;zxcvbnm,123456890swertyuiopdfghjkcvbnm"
    for i in ls:
        print(i) 
        time.sleep(2)

# printNum()
# alpha()

t1 = threading.Thread(target=printNum)
t2 = threading.Thread(target=alpha)

t1.start()
t2.start()

t1.join()
t2.join()