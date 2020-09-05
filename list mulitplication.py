l1=[]
l2=[]
l3=[]
list1=int(input('Enter the length of list 1 and list 2:-'))
for i in range(list1):
    value=int(input('Enter value'))
    l1.append(value)
print(l1)
for j in range(list1):
    value1=int(input('Enter values'))
    l2.append(value1)
print(l2)

for i in range(len(l1)):
    l3.append(l2[i]%l1[i])
print('Final list ')
print(l3)
print("doing merge")
