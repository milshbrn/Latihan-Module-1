import math
# def solve(hari):
#     tahun = math.floor(hari/360);
#     sisahari = hari%360;
#     bulan = math.floor(sisahari/30)
#     sisahari1 = sisahari%30;
#     minggu = math.floor(sisahari1/7);
#     sisahari2 = sisahari1%7;
#     hari = math.floor(sisahari2);

#     print("{} tahun {} bulan {} minggu {} hari".format(tahun,bulan,minggu,hari));

# solve(800)

# Cara Lain

total = 485;
tahun = math.floor(total/360);
bulan = math.floor(total%360)/30;
minggu = math.floor((total%360)%30)/7;
hari = math.floor(((total%360)%30)%7);

print(str(total) + 'Hari adalah');
print(str(tahun) + 'Tahun');
print(str(bulan) + 'Bulan');
print(str(minggu) + 'Minggu');
print(str(hari) + 'Hari');