#Operasi logika bolean 

#NOT ,OR ,AND

# not 
print('===NOT===')
a = False
c = not a
print ('data a = ', a)
print ('-------not')
print ('data c : ', c)

# OR 
print ('===OR===')
a = False
b = False
c = a or b 
print (a, 'or', b, '=', c)
a = False
b = True
c = a or b
print (a, 'or', b, '=', c)
a = True
b = False
c = a or b
print (a, 'or', b, '=', c)
a = True
b = True
c = a or b 
print (a, 'or', b, '=', c)

# AND - jika salah satu bernilai FALSE,hasil = FALSE 
print ('===AND===')
a = False
b = False
c = a and b
print (a, 'and', b, '=', c)
a = True
b = False
c = a and b
print (a, 'and', b, '=', c)
a = False
b = True
c = a and b
print (a, 'and', b, '=', c)
a = True
b = True
c = a and b
print (a, 'and', b, '=', c)
