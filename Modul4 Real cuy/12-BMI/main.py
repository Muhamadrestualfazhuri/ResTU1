#input tinggi badan
TinggiBadan = float(input('masukan tinggi badan dalam bentuk cm ='))
BeratBadan = float(input('masukan berat badan dalam bentuk kg='))

TinggiBadan = TinggiBadan / 100
BMI = BeratBadan / (TinggiBadan ** 2) 
BMI = f'BMI = {BMI:.1f}'
print(BMI)