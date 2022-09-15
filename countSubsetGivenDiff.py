from countSubsetSum import countSubsetSum

def countSubsetGivenDiff(arr, D):
    S = sum(arr)    
    s1 = S+D
    if s1%2: return 0
    s1 = s1//2

    return countSubsetSum(arr, s1)

if __name__=="__main__":
    print('Count of subset with given difference')
    arr = [1,2,3,4,5]
    D = 1
    print(countSubsetGivenDiff(arr, D))

    