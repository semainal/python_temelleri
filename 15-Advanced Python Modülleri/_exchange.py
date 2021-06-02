import requests 
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_doviz = input("Bozulan Döviz Türü: ")
alinan_doviz = input("Alınan Döviz Türü: ")

miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?: "))


result = requests.get(api_url + bozulan_doviz)
result = json.loads(result.text)
print(f"1 {bozulan_doviz} = {result['rates'][alinan_doviz]} {alinan_doviz}")
print(f"{miktar} {bozulan_doviz} = {miktar* result['rates'][alinan_doviz]} {alinan_doviz}")
