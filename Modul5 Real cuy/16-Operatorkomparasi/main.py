nilai = int(input("masukan nilaimu : "))

if nilai > 90:
    print("nilai kamu A")
elif nilai >= 85 and nilai < 90:
    print("nilai kamu A-")
elif nilai >= 80 and nilai < 85:
    print("nilai kamu B+")
elif nilai >= 75 and nilai < 80:
    print("nilai kamu B")
elif nilai >= 70 and nilai < 75:
    print("nilai kamu B-")
elif nilai >= 65 and nilai < 70:
    print("nilai kamu C+")
elif nilai >= 60 and nilai < 65:
    print("nilai kamu C")
elif nilai >= 55 and nilai < 60:
    print("nilai kamu D")
elif nilai < 55:
    print("nilai kamu E")