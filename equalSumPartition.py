from subsetSum import subsetSum  

def eqSumPart(arr):
    S = sum(arr)
    if S%2: return False
    S = S//2
    return subsetSum(arr, S)



if __name__=='__main__':
    print('Equal Sum partition')
    arr = [1,2,3,4]
    print(eqSumPart(arr))    


    