import pandas as pd


# customers = {
#     "CustomerId": [1,2,3,4],
#     "FirstName": ["Ahmet","Ali","Hasan","Canan"],
#     "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"],
# }

# orders = {
#     "OrderId": [10,11,12,13],
#     "CustomerId": [1,2,5,7],
#     "OrderDate": ["2021-10.06","2021-10.07","2021-10.08","2021-10.09"]
# }

# df_customers = pd.DataFrame(customers,columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])

# # print(df_customers)
# # print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner") # sadece customerId 1 ve 2 olan kayıtlar geldi.
# result = pd.merge(df_customers,df_orders,how="left") # siparişi olmayan müşteriler de geldi
# result = pd.merge(df_customers,df_orders,how="right") # orderlar gelir, müşteri bilgileri gelmez (databaseden silinmiş gibi)
# result = pd.merge(df_customers,df_orders,how="outer") # bütün kayıtlar getirilir.

customersA = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"],
}


customersB = {
    "CustomerId": [4,5,6,7],
    "FirstName": ["Yağmur","Çınar","Cengiz","Can"],
    "LastName": ["Bilge","Turan","Yılmaz","Turan"],
}


df_customersA = pd.DataFrame(customersA,columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerId","FirstName","LastName"])


result = pd.concat([df_customersA,df_customersB]) # listeyi birleştirip alt alta yazar
result = pd.concat([df_customersA,df_customersB], axis =1) # her yeni listeyi sağa yazar, yeni kolon oluşturur.


print(result)