# for num in range(1,21):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fizz"
#     if num % 5 == 0:
#         string = string + "Buzz"
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + str(num)
#     print(string)

# # Cara Lain
# def fizzBuzz(num) : 
#     for i in range(1,num+1) : 
#         if (i % 15 == 0) : 
#             print('FizzBuzz’); 
#         elif (i % 3 == 0) : 
#             print('Fizz’); 
#         elif (i % 5 == 0) : 
#             print('Buzz’); 
#         else : 
#             print(i);
# fizzBuzz(20);

# def fibo(urut) : 
#     listData = [1,1]; 
#     for i in range(2,urut): 
#         listData.append(listData[i-2] + listData[i-1]); 
#     return listData[urut-1];
# print(fibo(8));

# array=[1,2,3,4,5,6,7,8]
# array.reverse()
# print(array)
# Cara Lain 
# import math
# def reverseList(theList):
#     for i in range(math.floor(len(theList)/2)):
#         tempList = theList[i];
#         theList[i] = theList[len(theList) -1 -i];
#         theList[len(theList) -1 -i] = tempList
#     return theList

# listNya = [1,2,3,4,5,6,7,8]
# print(reverseList(listNya))

# import statistics;
# x = [1,2,3,2,5,2,7,2]
# print(statistics.mean(x))
# print(statistics.median(x))
# print(statistics.mode(x)) 


# def mean(theList):
#     return sum(theList) / len(theList);
   
# x = mean([1,2,3,2,5,2,7,2])
# print(x)

x = [1,2,3,2,5,2,7,2]
def median(list):
    list.sort();
    median = 0;
    if (len(list) % 2 != 0) : 
        median = list[floor(len(list) / 2)]; 
    else : mid1 = list[(int(len(list) / 2)) - 1]; mid2 = list[int(len(list) / 2)]; median = (mid1 + mid2) / 2; 
    return median;
print(median(x));




