myTuple = (4,2,1,3)
myList = ['one','two','three','four']
result = zip(myTuple,myList)
resultDict = dict(result)
sortedresult=sorted(resultDict)
print('unsorted Result',resultDict)
print("SortedResult",sortedresult)

resverseList = zip(myList,myTuple)
reverseListDict = dict(resverseList)
sotredReverseResult = sorted(reverseListDict)
print("#"*10)
print("sotredReverseResult",sotredReverseResult)

print("*"*10)
A0 = zip(('a','b','c','d','e'),[1,2,3,4,5]) 
A1 = dict(A0) 
A2 = sorted(A0)
print("unsortedDict: ",A1)
print("sorted Dict: ",A2)

