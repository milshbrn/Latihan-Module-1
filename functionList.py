def kali (x):
    if (x < 2):
        return 1;
    else :
        return (x * tiga());

def tiga():
    return 3;

print(kali(5));

# Contoh Recursive Function
def pangkat(x,y):
    if (y == 1):
        return x;
    else:
        y -= 1;
        return x * pangkat(x,y);

print(pangkat(2,4));


# Default Parameter
def kali(angka1 = 5, angka2 = 2):
    return angka1 * angka2;

print(kali(angka2 = 4));

# List append pop
buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga'];
buah.append('Kelapa'); 
print(buah); 
# append untuk masukin
# pop untuk ngeluarin
buah.pop();
buah.pop();
print(buah)

listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
print(listTest[1]);
print(listTest[:2]);
print(listTest[2]);
print(listTest[2][1:]);
print(listTest[2][2]);
print(listTest[2][3][0]);

# Sorted
x = [40,100,1,5,25,10]
i = sorted(x)
m = max(x)
a = min(x)

print(i)
print(m)
print(a)