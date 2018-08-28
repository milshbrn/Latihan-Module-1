print('Hello apa kabar');
print('Bro');


nama = 'Mila';
print(nama);

usia = 22;
usia = 32;
print(usia);

jomblo = True;
print(jomblo);

nama = 'Abi';
usia = 22;
jomblo = 'True';

print(type(nama));
print(type(usia));
print(type(jomblo));

# Latihan Intro to Python
nama = input("nama kamu? : ");
print("Nama : " + nama);
umur = input("umur kamu? : ");
print("Umur : " + umur);
kelamin = input("kelamin kamu? : ");
print("Kelamin : " + kelamin);
pekerjaan = input("pekerjaan kamu? : ");
print("Pekerjaan : " + pekerjaan);

#Cara buat function
def test(angka1):
    hasil = angka1 + angka1;
    return hasil;

num1 = 5;

jawaban = test(num1);
print(jawaban);


def mumet(angka2):
    hasil = angka2 + angka2;
    print(hasil);

mumet(12);

usiaAndi = 40;
usiaAndi = usiaAndi + 3;
print(usiaAndi);
   
usiaAndi = 40;
hasil = usiaAndi + 3;
print(usiaAndi);

# Number Aritmatics and Operator
usiaAndi = 40; 
usiaBudi = 20;
print(usiaAndi * usiaBudi); 
print(usiaAndi / usiaBudi); 
print(usiaAndi + usiaBudi); 
print(usiaAndi - usiaBudi); 
print(usiaAndi % usiaBudi); 
print(usiaBudi ** 2);

import math
print(math.pi); 
print(math.fabs(-4.7)); 
print(math.pow(8, 2));
print(math.sqrt(64))

x = 'Halo Dunia';
print(len(x)); 
print(x.index('Dunia')); 
print(x.split(' ')); 
print(x.lower()); 
print(x.upper()); 
print(x.capitalize());
