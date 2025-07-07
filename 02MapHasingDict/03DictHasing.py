num1=[3,5,3,2,1,5,7,8,5,5,3,7,9,7,3,3]
num2=[2,44,4,1,55,7,8,5]

hash_map={}

for i in range(0,len(num1)):
    hash_map[num1[i]]=hash_map.get(num1[i],0)+1

print(hash_map)
for j in num2:
    print(hash_map.get(j,0), end=",")

