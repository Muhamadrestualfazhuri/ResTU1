print ("SELAMAT DATANG DI TOKO AMBA")
print(30*"_")

member = input('apakah anda memiliki kartu member? ')
belanja = int(input('Masukan total belaja anda Rp.'))

if member == "ya" and belanja >= 500000:
    diskon =  belanja / 100 * 20
    total = belanja - diskon
    print(f'diskon yang kamu dapatkan : Rp.{diskon:.0f}')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "ya" and belanja < 500000:
    diskon =  belanja / 100 * 10
    total = belanja - diskon
    print(f'diskon yang kamu dapatkan : Rp.{diskon:.0f}')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "tidak" and belanja >= 500000:
    diskon =  belanja / 100 * 5
    total = belanja - diskon
    print(f'diskon yang kamu dapatkan : Rp.{diskon:.0f}')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "tidak" and belanja < 500000:
    total = belanja
    print (f'total belanjaan : Rp.{total:.0f}') 
print ("terima kasih telah berbelanja :)")