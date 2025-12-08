numList1 = [1,2,3,4,5]
numList2 = [6,7,8,9,10]

newList = []

for num in numList1:
    if num % 2 != 0 :
        newList.append(num)

for num in numList2:
    if num % 2 == 0 :
        newList.append(num)

print(newList)