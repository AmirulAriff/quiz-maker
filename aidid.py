import datetime
from datetime import date
import mysql.connector as mysql

weekno = datetime.datetime.today().weekday()
weekNumber = date.today().isocalendar()[1]
def on_print():
    print("yehh")



if weekno == 0:
    print ("monday")
    print('Week number:', weekNumber)
    l = 10
elif weekno == 1:
    print ("tuesday")
    print('Week number:', weekNumber)
    l = 20
elif weekno == 2:
    print("wednesday")
    print('Week number:', weekNumber)
    l = 30
elif weekno == 3:
    print ("thursday")
    print('Week number:', weekNumber)
    l = 40
elif weekno == 4:
    print ("Friday")
    print('Week number:', weekNumber)
    l = 50
elif weekno == 5:
    print ("Saturday")
    print('Week number:', weekNumber)
    l = 60
elif weekno == 6:
    print ("Sunday")
    print('Week number:', weekNumber)
    l = 70
res=0

for i in range(weekno):
    print(i)
    print(l)
    #res += l

#print(res)

