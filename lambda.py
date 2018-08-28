def sort(theList, fn):
    for i in range(len(theList));
        for j in range (i+1, len(theList));
        check = fn(theList[i], theList[j]);
        if(check > 0):
            temp = theList[i];
            theList[i] = theList[j];
            theList[j] = temp;

def minMax(theList):
    min = theList[0];
    max = theList[0];
    for i in range(1, len(theList)):
        if(min > the List[i]):
            min = theList[i];
        if(max < theList[i]):
            max = theList[i];

    return [min,max];

x = [40,100,1,5,25,100];

# def test(a,b):
#     return b-a;

test = lambda a,b: b-a;


sort(x, lambda a,b: a-b); //asc
print(x);
# sort(x,test); //desc 
sort(x,lambda a,b: b-a);
print(x);
# print(test)

theMinandMax

