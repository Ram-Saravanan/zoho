a = [50,9,3,4,66,10]

arr1 = list(map(str, a))

print(arr1)

for j in range(len(arr1)):
    swapped = False
    
    for i in range(len(arr1)-1):
        if arr1[i] + arr1[i+1] < arr1[i+1] + arr1[i]:
            arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
            swapped = True

    if not swapped:
        break            
        
print("corrent swap", arr1)     
print("the number is", "".join(arr1))