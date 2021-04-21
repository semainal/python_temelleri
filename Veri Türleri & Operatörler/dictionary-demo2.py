users = {}

number = input("kullanıcı no: ")
name = input("kullanıcı adı: ")
surname = input("kullanıcı soyadı: ")
email=input("kullancı email: ")
age=input("kullanıcı yaşı: ")

users[number] = {
"kullanıcı no": number,
"ad": name,
"soyad": surname,
"email": email,
"yaş": age}

print(users)