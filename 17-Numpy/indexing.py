import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])
result = numbers[5] #5.index
result = numbers[-1] # son index
result = numbers[0:3] #0-3 arası index 3 dahil değil
result = numbers[:3] # 0-3 arası index
result = numbers[3:] # 3.index dahil sonuna kadar 
result = numbers[::] # tüm liste
result = numbers[::-1] # listeyi ters çevirir
result = numbers[::-2] # listeyi ters çevirir 2şer atlayarak yazdırır

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0] # ilk grup eleman
result = numbers2[0,2] # 1.satırın 2.indexi 
result = numbers2[:,2] # : tüm satırların 2.indexleri
result = numbers2[:,0]
result = numbers2[:,0:2] # : tüm satırların 0-2 arası indexleri (0 dahil 2 dahil değil)
result = numbers2[-1,:] # tersten son satır
result = numbers2[:2,:2] # 1. ve 2. satırın 0.ve 1.indexleri

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 #referans
arr2 = arr1.copy() # arr1 kopyalandı

arr2[0] = 20 # değişiklik sadece arr2 de gerçekleşti
print(arr1)
print(arr2)
