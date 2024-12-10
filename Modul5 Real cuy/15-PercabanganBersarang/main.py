#Percabangan bersaranag / nested if
#kalkulator
#+,-,x,/,mod,//,pangkat(eksponen)

print(20*'=')
print('kalkulator sederhana')
print(20*'=')

angka_1 = float(input("masukan bilangan 1 = "))
operator = input('operator (+,-,x,/,mod,//,pangkat(eksponen)) : ')
angka_2 = float(input("masukan bilangan 2 = "))

#percabangan bersarang (elif statment)

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'Hasil nya adalah :{hasil}')
elif  operator == '-':
    hasil = angka_1 - angka_2
    print((hasil))
elif  operator == 'x':
    hasil = angka_1 * angka_2
    print((hasil))
elif  operator == '/':
    hasil = angka_1 / angka_2
    print((hasil))
elif  operator == '%' or operator == 'mod':
    hasil = angka_1 % angka_2
    print((hasil))
elif  operator == '//':
    hasil = angka_1 // angka_2
    print((hasil))
elif  operator == '**':
    hasil = angka_1 ** angka_2
    print((hasil))
