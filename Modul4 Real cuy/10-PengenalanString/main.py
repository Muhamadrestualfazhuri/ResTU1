#string adalah kumpulan dari karakter 

data=('inilah string')
print(data)
print('tipe data : ', len(data))
print('tipe data : ', type(data))

#1. cara membuat striang 

"""
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
"""

print("ini adalah hari jum'at")
#print('ini hari jum'at)
#2. kekuatan tanda \

#2. kukuatan \
# membuat ' menjadi string
print('saya sudah solat jum\'at')

# double backslash
print('c:\\user\\iam')

# tab (\t)
print("MU\t\tJuara")

# backspace (\b)
print ("MU\bJuara")

#new line (enter)
print('baris satu.\nbaris dua.') #LF -> line feed MacOS
print('baris satu.\n\rbaris dua.') #CRLF -> windows

# raw string
print(r'C:\User\aku')