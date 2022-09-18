array1= [1, 3, 5, 8]
array2 = [1, 2, 3]
k = 5
sortedArrays = sorted([*array1, *array2])[:k]
print(sortedArrays)