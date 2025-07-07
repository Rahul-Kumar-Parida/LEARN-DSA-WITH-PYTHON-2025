#method 1

nums=[1,2,3,4,4,5,5,8,8,8,2,1,1,3]

freq_map=dict()

for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1

print(freq_map)



#method 2  TC o(n)

hash_map={}

for i in range(0,len(nums)):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    #get give the value of dictionary, if not present then it return 0

print(hash_map)