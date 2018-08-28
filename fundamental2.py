# usia = 22;
# nama = 'Abi';

# print(usia + usia);
# print(nama + ' ' + nama);
# print(nama + ' ' + str(usia));

# if(False):
#      print('Hello');
# elif(False):
#     print('Apakabar');
# else :
#     print('Semua diatas salah');


# Solve 1
# angka = input("silahkan masukan angka berapapun: ");
# if(int(angka)%2==1):
#     print('Angka ini tergolong bilangan ganjil');
# else:
#     print('Angka ini tergolong bilangan genap')

# Solve 2
Massa = int(input("silahkan masukan massa anda: "));
Tinggi = int(input("silahkan masukan Tinggi Anda: "));

IMT = Massa / ((Tinggi/100)**2);
text = "";

if(IMT < 18.5):
    text = "BERAT BADAN KURANG";
elif(IMT >= 18.5 and IMT <= 24.9):
    text = "BERAT BADAN IDEAL";
elif(IMT >= 25.0 and IMT <= 29.9):
    text = "BERAT BADAN BERLEBIHAN";
elif(IMT >= 30.0 and IMT <= 39.9):
    text = "BERAT BADAN SANGAT BERLEBIH";
else:
    text = "OBESITAS";

print("Massa : " + str(Massa)  + ' ' + 'kg' + ' ' +  '&' +  ' ' + "Tinggi :" + str(Tinggi/100) + ' '  + 'M' );
print("IMT = " + str(IMT) + " " + text);