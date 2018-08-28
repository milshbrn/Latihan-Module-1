# listItem = list(range(1,11,2)); 
# print(listItem);
# for item in range(1,11,2): 
#     print(item)
# # Contoh Solve1
# for x in range(1,11):
#     print("nomer urut" + " " + str(x));

# # Contoh Solve2
# for x in range(0,21,2):
#     print("nomer urut" + " " + str(x));

# # Coba
# listTipe = ["Abi" , 22 , True , "Mila" , 21];
# for x in listTipe:
#     print(x)

# # Coba yuk 
# z = ""
# for x in range(5):
#     for y in range(5):
#         z += "*" + " "
#     z += '\n'
# print(z)

# # Solve 1
# z = "";
# for x in range(5):
#     for y in range(x+1,6):
#         z += ("*"+ " ");
#     z += '\n'
# print(z);

# Solve 2
# z = "";
# for x in range(4):
#     for y in range(x+1,6):
#         z += ("*"+ " ");
#     z += '\n'

# for a in range(5):
#     for m in range(0,a+1):
#         z += ("*"+ " ");
#     z += '\n'
# print(z);
 
# Coba Pake Inputan
# angka1 = input("silahkan masukan angka : ");
# angka2 = input("silahkan masukan angka berapapun: ");
# angka3 = input("silahkan masukan angka : ");
# angka4 = input("silahkan masukan angka berapapun: ");

# z = "";
# for x in range(int(angka1)):
#     for y in range(x+1,int(angka2)):
#         z += (" * "+ " ");
#     z += '\n'

# for a in range(int(angka3)):
#     for m in range(int(angka4),a+1):
#         z += (" * "+ " ");
#     z += '\n'
# print(z);

# Full Pyramid
# def fullPyramid(rows):
#     for x in range(rows):
#         print(' ' *(rows-x-1) + ' ' + '*'*(2*x+1))
# fullPyramid(10);

 

# Inverted Pyramid
# def InvertedPyramid(rows):
#     for y in reversed (range(rows)):
#         print(' ' *(rows-y-1) + ' ' + '*'*(2*y+1))

# InvertedPyramid(10);

