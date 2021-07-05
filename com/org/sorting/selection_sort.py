def selection(nums):
    for i in range(0,len(nums),1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [2,6,3,8,1,0,72,51,45,12,4]
print(f"Print Array Before sort {nums}")
selection(nums)
print(f"Print Array After sort {nums}")
