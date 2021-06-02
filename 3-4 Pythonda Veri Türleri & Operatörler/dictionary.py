#key & value

#41 => kocaeli 34=> istanbul

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("kocaeli")]) - sıralı olduğu için aynı index numarasıyla yazabildik.

# plakalar = {"istanbul" : 34, "kocaeli" : 41}
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# print(plakalar)

users = {
"Sema İnal" : 
 {"age" :35,
 "roles": ["admin", "user"],
  "email": "semainal35@gmail.com",
  "address": "izmir",
  "phone" : 5443217307 
 },

 "Tolga İnal":
 {"age": 35,
 "roles": ["user"],
 "email": "inal.tolga@gmail.com",
 "address": "istanbul",
 "phone": 5443217308
 }
}


print(users["Sema İnal"]["roles"])