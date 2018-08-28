gitmainMenu = ['1. Lihat Menu' '2. Lihat Cart' '3. Checkout' '4. Keluar']
menu = ['1. Paket Hoki A Rp 20.000', '2. Paket Hoki B Rp 25.000','3. Paket Hoki C Rp 30.000']
pilihmenu = []

def menulist():
    print('Selamat Datang di Hoki Hoki Bento')

def mainMenu():
   print('Main Menu')
   for y in main:
       print(y)

    pilih = int(input('silahkan masukan angka: '))
    if(pilih-1 == menu.index('1. Lihat Menu')):
        menuList()
    if(pilih-1 == menu.index('2. Lihat Cart')):
        menuList()
    if(pilih-1 == menu.index('3. Checkout')):
        menuList()
    if(pilih-1 == menu.index('4. Keluar')):
        menuList()


def menuItem():
    print('Menunya')
    for x in menu:
        print(x)

    pilihan = int(input('silahkan pilih menu: '))
    if(pilihan-1 == menu.index('1. Paket Hoki A Rp 20.000')):
        pilihmenu.append('Paket Hoki A Rp 20.000')
        mainMenu()
    if(pilihan-1 == menu.index('2. Paket Hoki B Rp 25.000')):
        pilihmenu.append('Paket Hoki B Rp 25.000')
        mainMenu()
    if(pilihan-1 == menu.index('3. Paket Hoki C Rp 30.000')):
        pilihmenu.append('Paket Hoki C Rp 30.000')
        mainMenu()

if(True):
    mainMenu()



    # Coba Yuk heheheh