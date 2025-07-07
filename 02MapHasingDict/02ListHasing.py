num1=[3,5,3,2,1,5,7,8,5,3,7,9,7,3,3]
num2=[2,44,4,1,55,7,8,7]

hash_list=[0]*11

for i in num1:
    hash_list[i]+=1

for j in num2:
    if j<0 or j>10:
        print(0, end=',')
    else:
        print(hash_list[j], end=',')
# print(hash_list)