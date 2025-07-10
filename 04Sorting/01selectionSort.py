#selection sort

lst=[4,7,2,7,8,1,9]

def selectionSort(nums):
    n=len(nums)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:  #for descending its >
                min_index=j
        if min_index!=i:
            nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums

print(selectionSort(lst))
        