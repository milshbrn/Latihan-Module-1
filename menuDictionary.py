def printMainMenu():
    inputUser = input('1. Lihat Semua Dictionary\n'+'2. Tambahkan New Dictionary\n'+'3. Filtering Isi Dictionary\n'+'4. Keluar\n' + 'Pilih Menu :')
    return inputUser


def satu():
   
    print(d);

def dua():
    key = input("Masukan Key yang diinginkan: ")
    value = input("Masukan value yang diinginkan : ");
    print("Key :" + key);
    print("value :" + value);

    d.update({key : value})
    print(d);


def tiga(item):
    inputUser = input("Search : ");
    filterDict = {k:v for (k,v) in d.items() if inputUser in k}
    

    for key in filterDict.keys():
        print('| ' +key + '|' + str(filterDict[key]))




d = {"Key" : "Values" , "test1" : 5 , "20" : 9 , "maruk" : [7,8]};
while True :
   pilihanuser = printMainMenu()
   if(pilihanuser == '1'):
       satu()
   elif(pilihanuser == '2'):
       dua()
   elif(pilihanuser == '3'):
       tiga(d)
   elif(pilihanuser == '4'):
       print('Terimakasih, Jangan Bosen dan Sampai Jumpa Lagi yaaa')
       break



# cara dari baron
# def mainMenu():
#    return input('1. Lihat Semua Dictionary\n'+'2. Tambahkan New Dictionary\n'+'3. Filtering Isi Dictionary\n'+'4. Keluar\n' + 'Pilih Menu :')

# def lihatFullDictionary (theDictionary):
#    print('Full Dictionary : ')
#    print('___________________________________________')
#    print('|        Key        |        Value        |')
#    print('____________________|______________________')
#    for key in theDictionary :
#        if(str(type(theDictionary[key])) == "<class 'str'>") :
#            print("|    " + key + "  |   '" + theDictionary[key] + "'   |" )
#        elif(str(type(theDictionary[key])) == "<class 'int'>") :
#            print("|    " + key + "  |   '" + str(theDictionary[key]) + "'   |" )

# def isiDictionary (theDictionary):
#    inputKey = input("Isi Key :")
#    inputJenis = input ("Value input 1 untuk string, 2 untuk number ? : ")
#    if(inputJenis=='1'):
#        inputValue = input("Valuenya : ")
#        theDictionary[inputKey] = inputValue
#    elif(inputJenis=='2') :
#        inputValue = input("Valuenya : ")
#        theDictionary[inputKey] = inputValue
#    else :
#        print( 'Bandel ya balik lagi gih ke menu')

# def searchDictionary (theDictionary):
#    inputSearch = input("Key Search : ")
#    newDDictionary = {}
#    for key in theDictionary:
#        if(inputSearch.lower() in key.lower()):
#            newDDictionary[key] = theDictionary[key]

#    lihatFullDictionary(newDDictionary)

# newDictionary = {}
# while True :
#    check = mainMenu()
#    if(check == '1'):
#        lihatFullDictionary(newDictionary)
#    elif(check == '2'):
#        isiDictionary(newDictionary)
#    elif(check == '3'):
#        searchDictionary(newDictionary)
#    elif(check == '4'):
#        print('Terimakasih, Jangan Bosen dan Sampai Jumpa Lagi yaaa')
#        break

