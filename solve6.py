import math 
jamAwal = 9
jarak = 120;
kecepatanTotal = 100/3600;
detikTotal = jarak / kecepatanTotal;
lamaJam = math.floor(detikTotal / 3600);
lamaMenit = math.floor(detikTotal%3600)/60;
lamaDetik = math.floor(detikTotal%3600)%60;

print('lama jam = ' + str(lamajam) + 'Lama Menit = ' + str(lamaMenit));
print('Tabrakannya Pukul' + str(jamAwal + lamaJam) + 'dan menit ke' str(lamaMenit) + 'dan detik ke' + str(lamaDetik));