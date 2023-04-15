# The 2 largest numbers in a sequence
#1,4,2,3,4,5,6
def MaxTwoNumber(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            maxSecond = max
            max = arr[i]
    
    print(maxSecond)
    print(max)


MaxTwoNumber([1,4,2,3,4,5,6])