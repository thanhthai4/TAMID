array1= [1, 3, 5, 8]
array2 = [1, 2, 3]
k = 5
#This function joins the 2 arrays into one array 
#sorts it & takes the first k numbers
sortedArrays = sorted([*array1, *array2])[:k]
print(sortedArrays)
