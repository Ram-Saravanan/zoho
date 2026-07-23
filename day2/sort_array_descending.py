a = [1,2,3,4,4,4,3,2,6,7]

dictionary = {}

for i in a:
    if i in dictionary:
        dictionary[i] += 1

    else:
        dictionary[i] = 1

print(dictionary)

sorted_arr = sorted(dictionary.items() ,key= lambda x:x[1], reverse= True)

for i in range(len(sorted_arr)):
    for j in range(sorted_arr[i][1]):
        print(sorted_arr[i][0], end = " ") 

# the sorted array with the descending values of the frequencies