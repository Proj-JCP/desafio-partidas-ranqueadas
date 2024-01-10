import datetime

date_now = datetime.datetime.now()
one_days_ago = date_now - datetime.timedelta(days=1)
print('now:', date_now.strftime("%d/%m/%y"))
print( one_days_ago.strftime("%d/%m/%y")) 