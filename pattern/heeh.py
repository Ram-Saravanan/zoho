nums = [1,2]
freq = {}    
arr1 = []
for i in nums:
    if i not in freq:
        freq[i] = 1

    else:
        freq[i] += 1
  

for keys, values in freq.items():
    if values > len(nums)/3:
        arr1.append(keys)

print(arr1)       
        