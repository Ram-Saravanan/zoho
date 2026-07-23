a = [1,2,3,4,4,4,3,2,6,7]

freq = {}

for i in a:
    #freq[i] = freq.get(i, 0) + 1 

    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1    

print(freq)

sorted_value = sorted((freq.items()) , key= lambda x:x[1], reverse = True)

for i in range(min(3, len(sorted_value))):
    print(sorted_value[i][0]) 

# top 3 repeated numbers acc to their freq