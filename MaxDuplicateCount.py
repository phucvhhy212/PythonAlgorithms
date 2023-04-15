# max duplicate character count in a string
def MaxDuplicateCount(input):
    count = 1
    maxCount = 1
    for x in range(len(input)-1):
        if input[x] == input[x+1]:
            count += 1
        else:
            count = 1
        if maxCount < count:
            maxCount = count
    
    return maxCount


print(MaxDuplicateCount("aaabbbdeefdddd"))  
