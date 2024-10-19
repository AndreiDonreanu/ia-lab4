import datetime
from xmlrpc.client import DateTime

import Customer,Visit,DiscountRate
from Customer import Customer
from Visit import Visit
client1=Customer("Gigel")
client1.set_member(True)
client1.set_member_type("premium")
print(client1)


data=datetime.date(2022,1,22)
vizita1=Visit(client1,data)


vizita1.set_product_expense(22.3)
vizita1.set_service_expense(15.7)

print(vizita1)

print(client1.get_name()+"trebuie sa plateasaca:"+"%s"%vizita1.get_total_expense(2,3))