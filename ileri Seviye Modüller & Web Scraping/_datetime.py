# from datetime import datetime
# from datetime import time
# from datetime import date

from datetime import datetime
from datetime import timedelta

# yukardakilerden istersen tek tek modülleri lazım olanı ekleyebilirsin.
#ya da direkt import datetime la bütün classları dahil edebilirisn.


simdi = datetime.now()
result = simdi.month


result = datetime.ctime(simdi)
result = datetime.strftime(simdi, "%d")
result = datetime.strftime(simdi, "%y %b %a")
print(result)


t = "1 April 2021 hour 16:50:17"

dt= datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)


birthday = datetime(1985,4,1,16,50,17)
print(birthday)

result = datetime.timestamp(birthday)
print(result)
result = datetime.fromtimestamp(result)
print(result)

result = datetime.fromtimestamp(0)

result = simdi - birthday

result = simdi + timedelta(days = 10)
result = simdi - timedelta(days = 10)
print(result)