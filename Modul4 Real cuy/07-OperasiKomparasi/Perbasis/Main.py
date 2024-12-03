#operasi komparasi

#setiap hasil selalu boolean (true/false)
  
#Lebih besar dari (>)
#Kurang dari (<)
#sama dengan (=)
#tidak sama dengan (!=)
#lebih dari sama dengan (>=)
#kurang dari sama dengan (<=)
#is
#dan is not

#deklarasi variable

a = 4 
b = 2

#Lebih besar dari (>)
print ('===Lebih besar dari (>)')
hasil = a > 2
print (a, '>', 2, '=', hasil)
hasil = b > 3 
print (b, '>', 3, '=', hasil)

#kurang dari (<)
print ('===kurang dari (<)')
hasil = a < 2
print (a, '<', 2, '=', hasil)
hasil = b < 3 
print (b, '<', 3, '=', hasil)

#Lebih dari sama dengan (>=)
print ('===Lebih dari sama dengan (>=)')
hasil = a >= 2
print (a, '>=', 2, '=', hasil)
hasil = b >= 3 
print (b, '>=', 3, '=', hasil)

#kurang dari sama dengan (<=)
print ('===kurang dari sama dengan(<=)')
hasil = a <= 2
print (a, '<=', 2, '=', hasil)
hasil = b <= 3 
print (b, '<=', 3, '=', hasil)

#sama dengan (==)
print ('===sama dengan (==)')
hasil = a == 2
print (a, '==', 2, '=', hasil)
hasil = b == 3 
print (b, '==', 3, '=', hasil)

#tidak sama dengan (!=)
print ('===tidak sama dengan (!=)')
hasil = a != 2
print (a, '!=', 2, '=', hasil)
hasil = b != 3 
print (b, '!=', 3, '=', hasil)

#is sebagai komparasi 

#angka adalah sebuah nilai literal yang artinya tidak di simpan di memory yang bisa adalah sebuah variable
# a = (angka) a adalah variable ygada di memory

x = 5
y = 5 
hasil = x is y 
print('nilai x : ', x,'id:', hex(id(x)))
print('nilai y : ', y,'id:', hex(id(y)))
print(x,'is:', y, '=', hasil)

#is not

x = 5
y = 5 
hasil = x is not y 
print('nilai x : ', x,'id:', hex(id(x)))
print('nilai y : ', y,'id:', hex(id(y)))
print(x,'is not:', y, '=', hasil)