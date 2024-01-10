import time
import datetime
date_now = datetime.datetime.now()
one_days_ago = date_now - datetime.timedelta(days=1)
tree_days_ago = date_now - datetime.timedelta(days=3)
seven_days_ago = date_now - datetime.timedelta(days=7)
print('now:', date_now.strftime("%d/%m/%y"))
print( one_days_ago.strftime("%d/%m/%y")) 
print( tree_days_ago.strftime("%d/%m/%y"))
print( seven_days_ago.strftime("%d/%m/%y"))

dt = datetime.datetime(year=2021, month=8, day=16)
str_dt = dt.strftime("%A")
print(str_dt)
weekday_name = ["SEG","TER","QUAR","QUI","SEX","SAB","DOM"]
wkday = dt.weekday()
print(weekday_name[wkday])
