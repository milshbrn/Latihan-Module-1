# d = { "key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"] };
# print(d["key1"]);
# print(d["key2"]); 
# print(d["kucing"]); 
# print(d["kucing"][1]);

# d = { "key1" : { "key2" : "item2" }, "kucing" : [3, "jerapah"] };
# print(d["key1"]); 
# print(d["key1"]["key2"]); 
# print(d["kucing"]);
# print(d["kucing"][1]);

# t = (1, [0, "test"], { "a1" : True },
# (0,{ "test" : 5 },2));
# print(t[3][1]["test"]);

# #  Pake Set biar datanya ga double
# s = { 1, 3, 1, 2, 2, 3 }; 
# print(s); 
# print(list(s)[2])

# newList = [1,3,"test2", "test1", 2, 3, "test2"];
# s = set(newList);

# print(s);
# newList1 = list(s);
# print(newList1);


# listNum = [1,2,3,4,5];
# listNum = [item * 2 for item in listNum];
# print(listNum);

# # without lambda pake function dan disimpan di memory
# def times2(num) : 
#     return num * 2;
# listNum = [ 1, 2, 3, 4, 5]; 
# listNum = list(map(times2, listNum)); 
# print(listNum);

# # with lamda 
# listNum = [ 1, 2, 3, 4, 5]; 
# listNum = list(map(lambda num: num * 2, listNum)); 
# print(listNum);

# # without filter
# def genap(num) : 
#     return num % 2 == 0;
# listNum = [ 1, 2, 3, 4, 5]; 
# listNum = list(filter(genap, listNum)); 
# print(listNum);

# # with filter. filter berfungsi untuk mereturn boolean. kalo false dihilangkan, kalo true ditampilkan.
# listNum = [ 1, 2, 3, 4, 5]; 
# listNum = list(filter(lambda num: num % 2 == 0, listNum)); 
# print(listNum);


# # Method for searching
# numList = [1,2,3]; 
# input = 'x';
# check1 = input in numList; 
# check2 = 'x' in ['x','y','z']; 
# check3 = 'ka' in 'kurakas';
# print(check1); 
# print(check2); 
# print(check3);


# Solve It
listData = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam'];
print(listData);
inputUser = input("Search : ");

def searchList(keyword,theList):
    newList = list(filter(lambda item: keyword.lower() in item.lower(), theList));
    return newList;

searchedList = searchList(inputUser,listData);
print(searchedList);
    



# kalo list pake kurung []
# kalo dictionaries pake kurung {} valuenya bisa diubah
# kalo tuples pake kurung () dan valuenya tidak bisa dirubah
# Didalam set tidak bisa pake list, dictionary. hanya bisa value dan tuples dikarenakan valuenya tidak pernah berubah.