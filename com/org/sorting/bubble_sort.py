
def bubble(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(0,i,1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [2,6,3,8,1,0,72,51,45,12,4]
print(f"Print Array Before sort {nums}")
bubble(nums)
print(f"Print Array After sort {nums}")
